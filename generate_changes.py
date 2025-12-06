#!/usr/bin/env python3
"""
Generate CHANGES.md from git commits that only touch solution Python files.

This script:
- Scans recent git commits
- Filters commits that only add/modify solution Python files
- Generates a formatted CHANGES.md file
"""

import subprocess
import re
import urllib.parse
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set, Optional
from urllib.parse import urlparse


class ChangesGenerator:
    """Generate CHANGES.md from git commits that only touch solution Python files."""
    
    # Solution file patterns
    SOLUTION_PATTERNS = [
        r'^leetcode/(easy|medium|hard)/.*\.py$',
        r'^deep-ml/(easy|medium)/.*\.py$',
        r'^codewars/kyu-\d+/.*\.py$',
        r'^aoc/\d{4}/day-\d{2}/solution_part_[12]\.py$',
    ]
    
    def __init__(self, path: str, limit: int):
        """
        Initialize the ChangesGenerator.
        
        Args:
            path: Path to the repository root directory
            limit: Maximum number of changes to include in the output
        """
        self.path = Path(path)
        self.limit = limit
    
    def is_solution_file(self, filepath: str) -> bool:
        """Check if a file path matches solution file patterns."""
        for pattern in self.SOLUTION_PATTERNS:
            if re.match(pattern, filepath):
                return True
        return False
    
    def get_commit_files(self, commit_hash: str) -> Dict[str, str]:
        """
        Get files changed in a commit with their status.
        Returns dict mapping filepath -> status (A=Added, M=Modified, D=Deleted).
        """
        try:
            result = subprocess.run(
                ['git', 'show', '--name-status', '--pretty=format:', commit_hash],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.path
            )
            
            files = {}
            for line in result.stdout.strip().split('\n'):
                if not line.strip():
                    continue
                # Format: STATUS\tFILEPATH
                parts = line.split('\t', 1)
                if len(parts) == 2:
                    status = parts[0]
                    filepath = parts[1]
                    # Handle renamed files (R100 old\tnew)
                    if status.startswith('R'):
                        # For renamed files, we care about the new name
                        filepath = parts[1].split('\t')[-1] if '\t' in parts[1] else parts[1]
                        status = 'M'  # Treat rename as modification
                    files[filepath] = status
            return files
        except subprocess.CalledProcessError:
            return {}
    
    def is_solution_only_commit(self, commit_hash: str) -> bool:
        """
        Check if a commit only touches solution files (additions or modifications).
        Returns True if commit only has solution file changes (A or M), False otherwise.
        """
        files = self.get_commit_files(commit_hash)
        
        if not files:
            return False
        
        solution_files = []
        non_solution_files = []
        
        for filepath, status in files.items():
            if self.is_solution_file(filepath):
                # Only include additions and modifications, not deletions
                if status in ('A', 'M'):
                    solution_files.append((filepath, status))
            else:
                non_solution_files.append((filepath, status))
        
        # Only include commits that:
        # 1. Have at least one solution file addition/modification
        # 2. Have NO non-solution files
        return len(solution_files) > 0 and len(non_solution_files) == 0
    
    def get_recent_commits(self, limit: int) -> List[Dict[str, str]]:
        """
        Get recent commits with their hash, date, and message.
        Returns list of dicts with keys: hash, date, message.
        """
        try:
            result = subprocess.run(
                ['git', 'log', f'--max-count={limit}', '--pretty=format:%H|%ai|%s'],
                capture_output=True,
                text=True,
                check=True,
                cwd=self.path
            )
            
            commits = []
            for line in result.stdout.strip().split('\n'):
                if not line.strip():
                    continue
                parts = line.split('|', 2)
                if len(parts) == 3:
                    commits.append({
                        'hash': parts[0],
                        'date': parts[1],
                        'message': parts[2]
                    })
            return commits
        except subprocess.CalledProcessError:
            return []
    
    def extract_complexity(self, file_path: str) -> tuple:
        """Extract time and space complexity from a file."""
        time_complexity = "N/A"
        space_complexity = "N/A"
        time_found = False
        space_found = False

        def parse_complexities(line):
            line = line.strip()
            time_complexity = "N/A"
            space_complexity = "N/A"

            time_idx = line.lower().find('time')
            space_idx = line.lower().find('space')

            def extract_complexity(start_search_idx, keyword_idx):
                start_idx = line.find('O(', start_search_idx, keyword_idx)
                if start_idx == -1:
                    return "N/A"
                end_idx = line.rfind(')', start_idx, keyword_idx)
                if end_idx == -1:
                    return "N/A"
                return line[start_idx:end_idx + 1].strip()

            if time_idx != -1 and space_idx != -1:
                if time_idx < space_idx:
                    time_complexity = extract_complexity(0, time_idx)
                    space_complexity = extract_complexity(time_idx, space_idx)
                else:
                    space_complexity = extract_complexity(0, space_idx)
                    time_complexity = extract_complexity(space_idx, time_idx)

                if space_complexity == 'N/A':
                    space_complexity = time_complexity
                if time_complexity == 'N/A':
                    time_complexity = space_complexity
            elif time_idx != -1:
                time_complexity = extract_complexity(0, time_idx)
            elif space_idx != -1:
                space_complexity = extract_complexity(0, space_idx)
            return time_complexity, space_complexity

        try:
            with open(file_path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line.startswith('#'):
                        time_complexity_tmp, space_complexity_tmp = parse_complexities(line)
                        if not time_found and time_complexity_tmp != "N/A":
                            time_found = True
                            time_complexity = time_complexity_tmp
                        if not space_found and space_complexity_tmp != "N/A":
                            space_found = True
                            space_complexity = space_complexity_tmp

                        if time_found and space_found:
                            break
        except:
            pass

        if '?' in time_complexity:
            time_complexity = "N/A"
        if '?' in space_complexity:
            space_complexity = "N/A"

        return time_complexity, space_complexity
    
    def extract_problem_link(self, file_path: str) -> str:
        """Extract problem source link from a file."""
        problem_link = "N/A"
        try:
            with open(file_path, 'r') as file:
                for line in file:
                    if re.search(r'(link:|source:)', line, re.IGNORECASE):
                        match = re.search(r'http[s]?://\S+', line)
                        if match:
                            problem_link = match.group(0).strip()
                            break
        except:
            pass
        return problem_link
    
    def extract_domain_name(self, url: str) -> str:
        """Extract domain name from a URL."""
        if url == "N/A":
            return "N/A"
        try:
            parsed_url = urlparse(url)
            domain = parsed_url.netloc
            domain_parts = domain.split('.')
            if len(domain_parts) >= 2:
                return '.'.join(domain_parts[-2:])
        except:
            pass
        return "N/A"
    
    def extract_challenge_name(self, filepath: str) -> str:
        """Extract challenge name from filepath."""
        parts = filepath.split('/')
        filename = parts[-1].replace('.py', '')
        
        if parts[0] == 'leetcode':
            # Remove leading number and separator (e.g., "3110. Score of a String" -> "Score of a String")
            match = re.match(r'^\d+[.\s]+(.+)$', filename)
            if match:
                return match.group(1)
            return filename
        elif parts[0] == 'deep-ml':
            # Remove leading number if present
            match = re.match(r'^\d+[.\s]+(.+)$', filename)
            if match:
                return match.group(1)
            return filename
        elif parts[0] == 'codewars':
            # Convert snake_case to Title Case
            return filename.replace('_', ' ').title()
        elif parts[0] == 'aoc':
            # For AoC, we'd need to read problem.txt, but for now use the part name
            return filename.replace('_', ' ').title()
        return filename
    
    def extract_type(self, filepath: str) -> str:
        """Extract type (platform + difficulty) from filepath."""
        parts = filepath.split('/')
        
        if parts[0] == 'leetcode' and len(parts) >= 2:
            difficulty = parts[1].capitalize()
            return f"LeetCode {difficulty}"
        elif parts[0] == 'deep-ml' and len(parts) >= 2:
            difficulty = parts[1].capitalize()
            return f"Deep-ML {difficulty}"
        elif parts[0] == 'codewars' and len(parts) >= 2:
            kyu = parts[1].replace('kyu-', 'Kyu ').title()
            return f"Codewars {kyu}"
        elif parts[0] == 'aoc' and len(parts) >= 3:
            year = parts[1]
            day = parts[2].replace('day-', 'Day ').title()
            return f"AoC {year} {day}"
        return parts[0] if parts else "Unknown"
    
    def format_file_link(self, filepath: str) -> str:
        """Format file path as markdown link."""
        encoded_path = urllib.parse.quote(filepath)
        return f"[python]({encoded_path})"
    
    def format_problem_link(self, link: str, domain: str) -> str:
        """Format problem link for markdown."""
        if link == "N/A":
            return 'N/A'
        return f'[{domain}]({link})'
    
    def generate_changes_md(self, commits: List[Dict[str, str]], limit: Optional[int]) -> str:
        """Generate markdown content for CHANGES.md in table format."""
        lines = [
            "## Recent Changes",
            "",
            "This file contains recent additions and updates to solution files.",
            "",
            "---",
            "",
        ]
        
        # Collect all changes (commits are already in reverse chronological order from git)
        all_changes = []
        for commit in commits:
            try:
                commit_datetime = datetime.strptime(commit['date'], '%Y-%m-%d %H:%M:%S %z')
                date_str = commit_datetime.strftime('%Y-%m-%d')
            except:
                commit_datetime = datetime.min
                date_str = commit['date'].split()[0] if commit['date'] else 'Unknown'

            files = self.get_commit_files(commit['hash'])
            solution_files = [
                (fp, status) for fp, status in files.items()
                if self.is_solution_file(fp) and status in ('A', 'M')
            ]

            for filepath, status in solution_files:
                file_full_path = self.path / filepath
                if not file_full_path.exists():
                    continue

                challenge = self.extract_challenge_name(filepath)
                type_str = self.extract_type(filepath)
                link = self.extract_problem_link(str(file_full_path))
                domain = self.extract_domain_name(link)

                all_changes.append({
                    'datetime': commit_datetime,
                    'date': date_str,
                    'type': type_str,
                    'challenge': challenge,
                    'solution_link': self.format_file_link(filepath),
                    'problem_link': self.format_problem_link(link, domain),
                })

        # Sort by datetime (newest first)
        all_changes.sort(key=lambda x: x['datetime'], reverse=True)

        # Limit to most recent N changes
        if limit is not None:
            all_changes = all_changes[:limit]
        
        # Generate single table
        lines.append("| Date | Type | Challenge | Solution Code | Problem Link |")
        lines.append("| --- | --- | --- | --- | --- |")

        for change in all_changes:
            lines.append(
                f"| {change['date']} | {change['type']} | {change['challenge']} | "
                f"{change['solution_link']} | {change['problem_link']} |"
            )
        
        lines.append("")
        
        return '\n'.join(lines)
    
    def has_solution_files(self, commit_hash: str) -> bool:
        """
        Check if a commit contains any solution file additions or modifications.
        Unlike is_solution_only_commit, this doesn't exclude commits with other files.
        """
        files = self.get_commit_files(commit_hash)

        for filepath, status in files.items():
            if self.is_solution_file(filepath) and status in ('A', 'M'):
                return True
        return False

    def generate(self) -> str:
        """
        Generate CHANGES.md content from git commits.

        Returns:
            String content of CHANGES.md
        """
        # Get recent commits (scan more than needed to find enough with solution files)
        all_commits = self.get_recent_commits(limit=100)

        # Filter to commits that contain solution files (may also contain other files)
        solution_commits = []
        for commit in all_commits:
            if self.has_solution_files(commit['hash']):
                solution_commits.append(commit)

        if not solution_commits:
            return "# Recent Changes\n\nNo recent changes to solution files.\n"

        return self.generate_changes_md(solution_commits, limit=self.limit)
    
    def generate_and_write(self, output_path: Path) -> None:
        """
        Generate CHANGES.md content and write it to a file.
        
        Args:
            output_path: Path where CHANGES.md should be written
        """
        content = self.generate()
        output_path.write_text(content, encoding='utf-8')
        print(f"Generated CHANGES.md with up to {self.limit} most recent changes")


if __name__ == '__main__':
    """Main function to generate CHANGES.md."""
    repo_path = Path(__file__).resolve().parent
    generator = ChangesGenerator(path=repo_path, limit=5)
    generator.generate_and_write(repo_path / 'CHANGES.md')
