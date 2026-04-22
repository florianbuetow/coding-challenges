#!/usr/bin/env python3
"""Fetch the last 10 accepted LeetCode submissions, display table, and cache solutions."""

import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

USERNAME = "sudoplz"
LIMIT = 15
GRAPHQL_URL = "https://leetcode.com/graphql"
COOKIE_FILE = Path(".cache/leetcode.cookie")
SOLUTIONS_DIR = Path(".cache/solutions")

UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) "
    "Version/17.4 Safari/605.1.15"
)

RECENT_QUERY = """
query recentAcSubmissions($username: String!, $limit: Int!) {
  recentAcSubmissionList(username: $username, limit: $limit) {
    id
    title
    titleSlug
    timestamp
  }
}
"""

QUESTION_QUERY = """
query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionFrontendId
    difficulty
  }
}
"""

SUBMISSION_QUERY = """
query submissionDetails($submissionId: Int!) {
  submissionDetails(submissionId: $submissionId) {
    code
    lang { name }
  }
}
"""

LANG_EXT = {
    "python": ".py", "python3": ".py",
    "cpp": ".cpp", "java": ".java",
    "javascript": ".js", "typescript": ".ts",
    "go": ".go", "rust": ".rs", "c": ".c",
}


class LeetCodeCache:
    def __init__(self, path: Path):
        self._path = path
        self._data: dict = {}
        self._dirty = False
        self._load()

    def _load(self):
        if self._path.exists():
            try:
                self._data = json.loads(self._path.read_text()).get("problems", {})
            except Exception:
                self._data = {}

    def get(self, slug: str):
        return self._data.get(slug)

    def set(self, slug: str, frontend_id: str, difficulty: str):
        self._data[slug] = {"id": frontend_id, "difficulty": difficulty}
        self._dirty = True

    def save(self):
        if not self._dirty:
            return
        self._path.parent.mkdir(exist_ok=True)
        self._path.write_text(json.dumps({"problems": self._data}, indent=2))
        self._dirty = False


def load_session():
    if session := os.environ.get("LEETCODE_SESSION"):
        return session
    if COOKIE_FILE.exists():
        for line in COOKIE_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                if k.strip() == "LEETCODE_SESSION":
                    return v.strip()
    return ""


def get_csrf(session):
    req = urllib.request.Request(
        "https://leetcode.com/accounts/login/",
        headers={
            "User-Agent": UA,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
            "Cookie": f"LEETCODE_SESSION={session}",
        },
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        for value in resp.headers.get_all("Set-Cookie") or []:
            for part in value.split(";"):
                part = part.strip()
                if part.startswith("csrftoken="):
                    return part.split("=", 1)[1]
    return ""


def graphql(query, variables, session="", csrf=""):
    cookie = "LEETCODE_SESSION=" + session if session else ""
    if csrf:
        cookie += f"; csrftoken={csrf}"
    req = urllib.request.Request(
        GRAPHQL_URL,
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={
            "Content-Type": "application/json",
            "User-Agent": UA,
            "Accept": "application/json",
            "Accept-Language": "en-US,en;q=0.9",
            "Referer": "https://leetcode.com/",
            "Cookie": cookie,
            "X-CSRFToken": csrf,
        },
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read())


def fetch_question(slug):
    data = graphql(QUESTION_QUERY, {"titleSlug": slug})
    q = data["data"]["question"]
    return slug, q["questionFrontendId"], q["difficulty"]


def solution_exists(frontend_id, difficulty):
    folder = Path("leetcode") / difficulty.lower()
    return any(folder.glob(f"{frontend_id}. *.py"))


def solution_cached(frontend_id):
    return bool(list(SOLUTIONS_DIR.glob(f"{frontend_id}. *")))


# --- fetch recent submissions ---
try:
    data = graphql(RECENT_QUERY, {"username": USERNAME, "limit": LIMIT})
except Exception as e:
    print(f"Error fetching submissions: {e}", file=sys.stderr)
    sys.exit(1)

submissions = data.get("data", {}).get("recentAcSubmissionList") or []
if not submissions:
    print(f"No recent accepted submissions found for '{USERNAME}'.")
    sys.exit(0)

# --- resolve problem metadata via cache or API ---
cache = LeetCodeCache(Path(".cache/leetcode_problems.json"))
details = {}
uncached = []

for sub in submissions:
    slug = sub["titleSlug"]
    entry = cache.get(slug)
    if entry:
        details[slug] = (entry["id"], entry["difficulty"])
    else:
        uncached.append(slug)

if uncached:
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(fetch_question, slug): slug for slug in uncached}
        for future in as_completed(futures):
            slug = futures[future]
            try:
                _, frontend_id, difficulty = future.result()
                details[slug] = (frontend_id, difficulty)
                cache.set(slug, frontend_id, difficulty)
            except Exception:
                details[slug] = ("?", "?")
    cache.save()

# --- build table rows ---
rows = []
for i, sub in enumerate(submissions, 1):
    slug = sub["titleSlug"]
    frontend_id, difficulty = details.get(slug, ("?", "?"))
    problem = f"{frontend_id}. {sub['title']}"
    url = f"https://leetcode.com/problems/{slug}/"
    local = "yes" if solution_exists(frontend_id, difficulty) else "-"
    date = datetime.fromtimestamp(int(sub["timestamp"]), tz=timezone.utc).strftime("%Y-%m-%d")
    rows.append((str(i), date, problem, difficulty, url, local))

# --- render table ---
col_headers = ("#", "Date", "Problem", "Difficulty", "URL", "Local")
widths = [
    max(len(col_headers[c]), max(len(r[c]) for r in rows))
    for c in range(6)
]

H, V = "─", "│"
TL, TR, BL, BR = "┌", "┐", "└", "┘"
ML, MR, MT, MB, MC = "├", "┤", "┬", "┴", "┼"

DIFF_COLOR = {"Easy": "\033[0;32m", "Medium": "\033[0;33m", "Hard": "\033[0;31m"}
DIFF_COL = col_headers.index("Difficulty")
RESET = "\033[0m"

def top(w):    return TL + MT.join(H * (n + 2) for n in w) + TR
def mid(w):    return ML + MC.join(H * (n + 2) for n in w) + MR
def bottom(w): return BL + MB.join(H * (n + 2) for n in w) + BR

def row(cells, w):
    parts = []
    for i, (c, n) in enumerate(zip(cells, w)):
        color = DIFF_COLOR.get(c) if i == DIFF_COL else None
        padded = f"{color}{c}{RESET}" + " " * (n - len(c)) if color else c.ljust(n)
        parts.append(f" {padded} ")
    return V + V.join(parts) + V

print()
print(top(widths))
print(row(col_headers, widths))
print(mid(widths))
for r in rows:
    print(row(r, widths))
print(bottom(widths))
print()

# --- download missing solutions ---
to_download = [
    sub for sub in submissions
    if not solution_cached(details.get(sub["titleSlug"], ("?",))[0])
]
if not to_download:
    sys.exit(0)

session = load_session()
if not session:
    print(f"Error: LEETCODE_SESSION not set. Add it to {COOKIE_FILE}.", file=sys.stderr)
    sys.exit(1)

try:
    csrf = get_csrf(session)
except Exception as e:
    print(f"Error: could not fetch CSRF token: {e}", file=sys.stderr)
    sys.exit(1)

SOLUTIONS_DIR.mkdir(parents=True, exist_ok=True)
for sub in to_download:
    slug = sub["titleSlug"]
    frontend_id, _ = details.get(slug, ("?", "?"))
    filename_stem = f"{frontend_id}. {sub['title']}"
    try:
        result = graphql(SUBMISSION_QUERY, {"submissionId": int(sub["id"])}, session, csrf)
        details_sub = result["data"]["submissionDetails"]
        ext = LANG_EXT.get(details_sub["lang"]["name"], ".txt")
        (SOLUTIONS_DIR / f"{filename_stem}{ext}").write_text(details_sub["code"])
        print(f"  cached {filename_stem}{ext}")
    except Exception as e:
        print(f"  error  {filename_stem}: {e}", file=sys.stderr)

print()
