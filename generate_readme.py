import os
import re
import urllib.parse
from urllib.parse import urlparse
from pathlib import Path
from generate_changes import ChangesGenerator


class BaseChallengeProcessor:
    """Base class providing shared utility methods for all challenge processors."""

    def extract_complexity(self, file_path):
        """Extract time and space complexity from a file."""
        time_complexity = "N/A"
        space_complexity = "N/A"
        time_found = False
        space_found = False

        def parse_complexities(line):
            line = line.strip()
            time_complexity = "N/A"
            space_complexity = "N/A"

            # Find positions of 'time' and 'space' in lowercase for case-insensitivity
            time_idx = line.lower().find('time')
            space_idx = line.lower().find('space')

            # Nested function to extract complexity from 'O(' to the last ')' before a keyword
            def extract_complexity(start_search_idx, keyword_idx):
                start_idx = line.find('O(', start_search_idx, keyword_idx)
                if start_idx == -1:
                    return "N/A"
                # Find the rightmost closing bracket before the keyword
                end_idx = line.rfind(')', start_idx, keyword_idx)
                if end_idx == -1:
                    return "N/A"
                return line[start_idx:end_idx + 1].strip()

            # Case 1 and 2: Both "time" and "space" keywords are present
            if time_idx != -1 and space_idx != -1:
                if time_idx < space_idx:
                    # Case 1: "O(...) time ... O(...) space"
                    time_complexity = extract_complexity(0, time_idx)
                    space_complexity = extract_complexity(time_idx, space_idx)
                else:
                    # Case 2: "O(...) space ... O(...) time"
                    space_complexity = extract_complexity(0, space_idx)
                    time_complexity = extract_complexity(space_idx, time_idx)

                # Case 3 and 4: Only one complexity, applying to both "time" and "space"
                if space_complexity == 'N/A': space_complexity = time_complexity
                if time_complexity == 'N/A': time_complexity = space_complexity

            # Case 5: Only "time" is specified
            elif time_idx != -1:
                time_complexity = extract_complexity(0, time_idx)

            # Case 6: Only "space" is specified
            elif space_idx != -1:
                space_complexity = extract_complexity(0, space_idx)
            return time_complexity, space_complexity

        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()

                # Check if the line is a comment
                if line.startswith('#'):
                    # Extract complexity if any O(...) notation exists
                    time_complexity_tmp, space_complexity_tmp = parse_complexities(line)
                    if not time_found and time_complexity_tmp != "N/A":
                        time_found = True
                        time_complexity = time_complexity_tmp
                    if not space_found and space_complexity_tmp != "N/A":
                        space_found = True
                        space_complexity = space_complexity_tmp

                if time_found and space_found:
                    break

        # Normalize "?" to "N/A"
        if '?' in time_complexity:
            time_complexity = "N/A"
        if '?' in space_complexity:
            space_complexity = "N/A"

        return time_complexity, space_complexity

    def extract_problem_link(self, file_path):
        """Extract problem source link from a file."""
        problem_link = "N/A"

        with open(file_path, 'r') as file:
            for line in file:
                if re.search(r'(link:|source:)', line, re.IGNORECASE):
                    match = re.search(r'http[s]?://\S+', line)
                    if match:
                        problem_link = match.group(0).strip()
                        break

        return problem_link

    def extract_domain_name(self, url):
        """Extract domain name from a URL."""
        parsed_url = urlparse(url)
        domain = parsed_url.netloc
        # Extract only the main domain part, without subdomains
        domain_parts = domain.split('.')
        if len(domain_parts) >= 2:
            return '.'.join(domain_parts[-2:])
        return "N/A"

    def _format_problem_link(self, problem):
        """Format problem link for markdown."""
        if 'N/A' in problem["problem_link"]:
            return 'N/A'
        else:
            return f'[{problem["problem_domain"]}]({problem["problem_link"]})'

    def generate_markdown(self, root_dir, folder_path):
        """Generate markdown section. Must be implemented by subclasses."""
        raise NotImplementedError


class TwoLevelProcessor(BaseChallengeProcessor):
    """Base class for processors with 2-level structure: {platform}/{difficulty}/{file}.py"""

    def generate_markdown(self, root_dir, folder_path):
        """Generate markdown for 2-level folder structure."""
        folder_name = os.path.basename(folder_path)
        subfolders = {}
        
        for subfolder in os.listdir(folder_path):
            subfolder_path = os.path.join(folder_path, subfolder)
            if os.path.isdir(subfolder_path):
                problems = []
                filenames = sorted(os.listdir(subfolder_path))
                for idx, filename in enumerate(filenames):
                    if filename.endswith('.py'):
                        problem_name = filename.replace('.py', '')
                        file_path = os.path.join(subfolder_path, filename)
                        relative_path = os.path.relpath(file_path, root_dir)
                        url_encoded_path = urllib.parse.quote(relative_path)

                        # Extract time and space complexity
                        time_complexity, space_complexity = self.extract_complexity(file_path)

                        # Extract problem source link
                        problem_link = self.extract_problem_link(file_path)
                        problem_domain = self.extract_domain_name(problem_link)

                        # Extract problem number from filename or use list index + 1
                        match = re.match(r'^(\d+)(\S*)', filename)
                        problem_number = match.group(1) if match else str(idx + 1)

                        # Remove the number and non-whitespace characters that follow it from the challenge name
                        if match:
                            problem_name = problem_name[len(match.group(0)):].strip()

                        problems.append({
                            "problem_number": problem_number,
                            "challenge": problem_name,
                            "time": time_complexity,
                            "space": space_complexity,
                            "solution_link": url_encoded_path,
                            "solution_lang": 'python',
                            "problem_domain": problem_domain,
                            "problem_link": problem_link
                        })
                if problems:
                    problems = sorted(problems, key=lambda x: int(x["problem_number"]))
                    subfolders[subfolder] = problems

        if not subfolders:
            return ""

        # Generate markdown
        markdown = []
        section_title = folder_name.capitalize()
        markdown.append(f'# {section_title}\n')
        
        for subfolder in sorted(subfolders):
            problems = subfolders[subfolder]
            markdown.append(f'### {subfolder.capitalize()}\n')
            markdown.append('| Nr. | Challenge | Time Complexity | Space Complexity | Solution Code | Problem Link |\n')
            markdown.append('| --- | --- | --- | --- | --- | --- |\n')
            for problem in problems:
                problem_md_link = self._format_problem_link(problem)
                markdown.append(f'| {problem["problem_number"]} | {problem["challenge"]} '
                               f'| {problem["time"]} | {problem["space"]} '
                               f'| [{problem["solution_lang"]}]({problem["solution_link"]}) '
                               f'| {problem_md_link} |\n')
            markdown.append('\n')

        return ''.join(markdown)


class LeetCodeProcessor(TwoLevelProcessor):
    """Processor for LeetCode challenges."""
    pass


class DeepMLProcessor(TwoLevelProcessor):
    """Processor for Deep-ML challenges."""
    pass


class AdventOfCodeProcessor(BaseChallengeProcessor):
    """Processor for Advent of Code challenges with 3-level structure: aoc/year/day-XX/"""

    def extract_aoc_challenge_name(self, day_path):
        """
        Parse problem.txt to extract challenge name from line like:
        '--- Day 6: Trash Compactor ---'
        Returns the challenge name (e.g., 'Trash Compactor') or None if not found.
        """
        problem_file = os.path.join(day_path, 'problem.txt')
        if not os.path.exists(problem_file):
            return None

        with open(problem_file, 'r') as f:
            first_line = f.readline().strip()

        # Match pattern: --- Day X: Challenge Name ---
        match = re.match(r'^---\s*Day\s+\d+:\s*(.+?)\s*---$', first_line)
        if match:
            return match.group(1)
        return None

    def generate_markdown(self, root_dir, folder_path):
        """Generate markdown for AoC folder structure."""
        sections = {}

        for year in os.listdir(folder_path):
            year_path = os.path.join(folder_path, year)
            if not os.path.isdir(year_path) or year.startswith('.'):
                continue

            problems = []
            for day_folder in os.listdir(year_path):
                day_path = os.path.join(year_path, day_folder)
                if not os.path.isdir(day_path) or day_folder.startswith('.'):
                    continue

                # Extract day number from "day-06" format
                day_match = re.match(r'day-(\d+)', day_folder)
                if not day_match:
                    continue
                day_num = int(day_match.group(1))
                day_num_padded = str(day_num).zfill(2)
                date_str = f"{year}-12-{day_num_padded}"  # AoC runs in December

                # Extract challenge name from problem.txt
                challenge_name = self.extract_aoc_challenge_name(day_path)

                # Process solution_part_1.py and solution_part_2.py
                for part in [1, 2]:
                    filename = f"solution_part_{part}.py"
                    filepath = os.path.join(day_path, filename)
                    if not os.path.exists(filepath):
                        continue

                    # Skip empty solution files
                    if os.path.getsize(filepath) == 0:
                        continue

                    time_c, space_c = self.extract_complexity(filepath)
                    link = self.extract_problem_link(filepath)
                    domain = self.extract_domain_name(link)
                    relative_path = os.path.relpath(filepath, root_dir)

                    # Build challenge display name
                    if challenge_name:
                        challenge_display = f"{challenge_name} {part}/2"
                    else:
                        challenge_display = f"Day {day_num} {part}/2"

                    problems.append({
                        "problem_number": day_num,
                        "sort_key": (date_str, part),
                        "challenge": challenge_display,
                        "time": time_c,
                        "space": space_c,
                        "solution_link": urllib.parse.quote(relative_path),
                        "solution_lang": "python",
                        "problem_domain": domain,
                        "problem_link": link
                    })

            # Sort: day ascending, then part ascending
            if problems:
                problems.sort(key=lambda x: (x['problem_number'], x['sort_key'][1]))
                sections[year] = problems

        if not sections:
            return ""

        # Generate markdown
        markdown = []
        markdown.append('# Advent of Code\n')
        
        for year in sorted(sections):
            problems = sections[year]
            markdown.append(f'### {year.capitalize()}\n')
            markdown.append('| Day | Challenge | Time Complexity | Space Complexity | Solution Code | Problem Link |\n')
            markdown.append('| --- | --- | --- | --- | --- | --- |\n')
            for problem in problems:
                problem_md_link = self._format_problem_link(problem)
                markdown.append(f'| {problem["problem_number"]} | {problem["challenge"]} '
                               f'| {problem["time"]} | {problem["space"]} '
                               f'| [{problem["solution_lang"]}]({problem["solution_link"]}) '
                               f'| {problem_md_link} |\n')
            markdown.append('\n')

        return ''.join(markdown)


class CodewarsProcessor(BaseChallengeProcessor):
    """Processor for Codewars challenges with kyu-based structure."""

    def generate_markdown(self, root_dir, folder_path):
        """Generate markdown for Codewars folder structure."""
        sections = {}

        for kyu_folder in os.listdir(folder_path):
            kyu_path = os.path.join(folder_path, kyu_folder)
            if not os.path.isdir(kyu_path) or kyu_folder.startswith('.'):
                continue

            # Extract kyu level from "kyu-4" format
            kyu_match = re.match(r'kyu-(\d+)', kyu_folder)
            if not kyu_match:
                continue
            kyu_level = int(kyu_match.group(1))

            problems = []
            for filename in os.listdir(kyu_path):
                if not filename.endswith('.py'):
                    continue

                filepath = os.path.join(kyu_path, filename)

                # Skip empty files
                if os.path.getsize(filepath) == 0:
                    continue

                # Convert snake_case filename to Title Case challenge name
                problem_name = filename.replace('.py', '')
                challenge_display = problem_name.replace('_', ' ').title()

                time_c, space_c = self.extract_complexity(filepath)
                link = self.extract_problem_link(filepath)
                domain = self.extract_domain_name(link)
                relative_path = os.path.relpath(filepath, root_dir)

                problems.append({
                    "challenge": challenge_display,
                    "time": time_c,
                    "space": space_c,
                    "solution_link": urllib.parse.quote(relative_path),
                    "solution_lang": "python",
                    "problem_domain": domain,
                    "problem_link": link
                })

            # Sort alphabetically by challenge name
            if problems:
                problems.sort(key=lambda x: x['challenge'].lower())
                sections[kyu_folder] = problems

        if not sections:
            return ""

        # Generate markdown
        markdown = []
        markdown.append('# Codewars\n')
        
        for kyu_folder in sorted(sections):
            problems = sections[kyu_folder]
            markdown.append(f'### {kyu_folder.capitalize()}\n')
            markdown.append('| Challenge | Time Complexity | Space Complexity | Solution Code | Problem Link |\n')
            markdown.append('| --- | --- | --- | --- | --- |\n')
            for problem in problems:
                problem_md_link = self._format_problem_link(problem)
                markdown.append(f'| {problem["challenge"]} '
                               f'| {problem["time"]} | {problem["space"]} '
                               f'| [{problem["solution_lang"]}]({problem["solution_link"]}) '
                               f'| {problem_md_link} |\n')
            markdown.append('\n')

        return ''.join(markdown)


class ReadmeGenerator:
    """Main class for generating README.md from challenge solutions."""

    def __init__(self):
        """Initialize processor registry."""
        self.processors = {
            'leetcode': LeetCodeProcessor(),
            'deep-ml': DeepMLProcessor(),
            'aoc': AdventOfCodeProcessor(),
            'codewars': CodewarsProcessor()
        }

    def read_file(self, filename):
        """Read content from a file, raising an error if it doesn't exist."""
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return file.read().strip()
        else:
            raise FileNotFoundError(f"Error: {filename} not found. Please ensure it exists in the project directory.")

    def generate_stats_table(self, root_dir):
        """Generate a stats table with metrics per category."""
        stats = []

        # Iterate through platform folders (leetcode, codewars, aoc, deep-ml)
        for platform in os.listdir(root_dir):
            platform_path = os.path.join(root_dir, platform)
            if not os.path.isdir(platform_path) or platform.startswith('.'):
                continue
            if platform not in self.processors:
                continue

            # Iterate through subcategory folders
            for subcategory in os.listdir(platform_path):
                subcat_path = os.path.join(platform_path, subcategory)
                if not os.path.isdir(subcat_path) or subcategory.startswith('.'):
                    continue

                # Collect all Python files recursively
                py_files = []
                for dirpath, _, filenames in os.walk(subcat_path):
                    for f in filenames:
                        if f.endswith('.py'):
                            py_files.append(os.path.join(dirpath, f))

                if not py_files:
                    continue

                # Calculate metrics
                total_loc = 0
                while_count = 0
                for_count = 0
                if_count = 0
                break_count = 0
                continue_count = 0
                heapq_count = 0
                deque_count = 0
                set_count = 0
                list_count = 0
                dict_count = 0

                for py_file in py_files:
                    with open(py_file, 'r') as f:
                        content = f.read()
                        lines = content.splitlines()
                        total_loc += len(lines)
                        # Simple text search
                        while_count += len(re.findall(r'\bwhile\b', content))
                        for_count += len(re.findall(r'\bfor\b', content))
                        if_count += content.count('if ')
                        break_count += len(re.findall(r'\bbreak\b', content))
                        continue_count += len(re.findall(r'\bcontinue\b', content))
                        heapq_count += content.count('heapq')
                        deque_count += content.count('deque')
                        set_count += content.count('set(')
                        list_count += content.count('list(')
                        dict_count += content.count('= {') + content.count('dict(')

                avg_loc = total_loc // len(py_files) if py_files else 0

                stats.append({
                    'category': f"{platform}-{subcategory}",
                    'solves': len(py_files),
                    'loc': total_loc,
                    'avg_loc': avg_loc,
                    'while': while_count,
                    'for': for_count,
                    'if': if_count,
                    'break': break_count,
                    'continue': continue_count,
                    'heapq': heapq_count,
                    'deque': deque_count,
                    'set': set_count,
                    'list': list_count,
                    'dict': dict_count
                })

        # Sort by category name
        stats.sort(key=lambda x: x['category'])

        # Generate markdown table
        lines = [
            "## Stats\n\n",
            "| Category | Solves | LOC | Avg LOC | while | for | if | break | continue | heapq | deque | set | list | dict |\n",
            "|----------|--------|-----|---------|-------|-----|------|-------|----------|-------|-------|-----|------|------|\n"
        ]
        for s in stats:
            lines.append(f"| {s['category']} | {s['solves']} | {s['loc']} | {s['avg_loc']} | {s['while']} | {s['for']} | {s['if']} | {s['break']} | {s['continue']} | {s['heapq']} | {s['deque']} | {s['set']} | {s['list']} | {s['dict']} |\n")
        lines.append("\n")

        return ''.join(lines)

    def generate(self, root_dir):
        """Generate the README.md file."""
        project_description = self.read_file('DESCRIPTION.md')
        project_usage = self.read_file('USAGE.md')

        readme_file = os.path.join(root_dir, 'README.md')

        markdown_sections = []

        for folder in os.listdir(root_dir):
            if folder.startswith('.'):
                continue
            folder_path = os.path.join(root_dir, folder)
            if not os.path.isdir(folder_path):
                continue

            # Use dedicated processor if available
            if folder in self.processors:
                markdown = self.processors[folder].generate_markdown(root_dir, folder_path)
                if markdown:
                    markdown_sections.append((folder, markdown))

        # Sort sections by folder name to maintain consistent order
        markdown_sections.sort(key=lambda x: x[0])

        # Read recent changes content from CHANGES.md
        changes_content = self.read_file('CHANGES.md')

        with open(readme_file, 'w') as readme:
            readme.write('# Coding-Challenges\n\n')
            readme.write(f'{project_description}\n\n')
            stats_table = self.generate_stats_table(root_dir)
            readme.write(stats_table)
            readme.write(f'{changes_content}\n')

            for folder, markdown in markdown_sections:
                readme.write(markdown)

            readme.write(f'{project_usage}\n\n')


if __name__ == '__main__':
    # Generate CHANGES.md FIRST (so README.md gets the fresh content)
    changes_generator = ChangesGenerator(path=Path("./"), limit=10)
    changes_generator.generate_and_write(Path("./CHANGES.md"))

    # Then generate README.md (which reads the freshly created CHANGES.md)
    generator = ReadmeGenerator()
    generator.generate("./")
