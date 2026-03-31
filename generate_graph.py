#!/usr/bin/env python3
"""Generate a cumulative graph of coding challenge solutions over time."""

import subprocess
import re
import pandas as pd
import plotly.express as px

# Get all .py files added in git history with their dates
result = subprocess.run(
    ["git", "log", "--diff-filter=A", "--name-only", "--pretty=format:%ad", "--date=short", "--", "*.py"],
    capture_output=True, text=True
)

# Parse git output into (date, filepath) pairs
solution_dirs = {"leetcode/": "LeetCode", "deep-ml/": "Deep-ML", "codewars/": "Codewars", "aoc/": "AoC"}
date = None
records = []

for line in result.stdout.splitlines():
    line = line.strip()
    if not line:
        continue
    if re.match(r"^\d{4}-\d{2}-\d{2}$", line):
        date = line
    elif date:
        for prefix, label in solution_dirs.items():
            if line.startswith(prefix):
                records.append({"Date": date, "Category": label})
                break

# Build dataframe sorted by date
df = pd.DataFrame(records)
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date").reset_index(drop=True)
df["Solutions"] = range(1, len(df) + 1)

# Create line chart with colored dots per category
fig = px.scatter(
    df, x="Date", y="Solutions", color="Category",
    title="Coding Challenge Solutions Over Time",
    labels={"Solutions": "Total Solutions", "Date": "Date"},
    color_discrete_map={"LeetCode": "#FFA116", "Deep-ML": "#E91E63", "Codewars": "#B1361E", "AoC": "#FFDF00"},
)
fig.add_scatter(x=df["Date"], y=df["Solutions"], mode="lines", line=dict(color="gray", width=1), showlegend=False)

# Avg problems/month for each calendar day: total solved up to day x / months elapsed
start = df["Date"].iloc[0]
all_days = pd.date_range(start, df["Date"].iloc[-1], freq="D")
cumulative = all_days.to_series().apply(lambda d: (df["Date"] <= d).sum())
months_elapsed = (all_days - start).days / 30
# Start after first full month to avoid initial instability
mask = months_elapsed >= 1
fig.add_scatter(x=all_days[mask], y=(cumulative[mask].values / months_elapsed[mask]), mode="lines",
                name="Avg problems/mo", line=dict(color="gray", width=2, dash="dash"), yaxis="y2")

fig.update_layout(
    title={"text": "Coding Challenge Solutions Over Time", "x": 0.5, "xanchor": "center"},
    xaxis_title="Date",
    yaxis_title="Total Solutions (cumulative)",
    xaxis=dict(showline=True, linewidth=1, linecolor="black", mirror=False,
               ticks="outside", ticklen=5, dtick="M1", tickformat="%b %Y"),
    yaxis=dict(showline=True, linewidth=1, linecolor="black", mirror=False,
               ticks="outside", ticklen=5, dtick=50),
    yaxis2=dict(title="Avg problems/month", showline=True, linewidth=1, linecolor="gray",
                ticks="outside", ticklen=5, overlaying="y", side="right"),
)
fig.update_traces(cliponaxis=False)

# Save as PNG
fig.write_image("solutions_growth.png", width=1024, height=683)

print(f"Total solutions: {df['Solutions'].iloc[-1]}")
print(f"Date range: {df['Date'].iloc[0].date()} to {df['Date'].iloc[-1].date()}")
print("Chart saved: solutions_growth.png")
