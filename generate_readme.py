import os
import re
import urllib.parse
from urllib.parse import urlparse


# Function to extract time and space complexity from a file
def extract_complexity(file_path):
    time_complexity = "N/A"
    space_complexity = "N/A"
    time_found = False
    space_found = False

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()

            # Check if the line is a comment
            if line.startswith('#'):
                # Look for space complexity
                if not space_found and re.search(r'\bspace\b', line, re.IGNORECASE):
                    rightmost_space_idx = line.rfind('O(', 0, line.lower().find('space'))
                    if rightmost_space_idx != -1:
                        space_complexity = re.search(r'O\([^)]*(?:\([^)]*\))*\)', line[rightmost_space_idx:]).group(0).strip()
                        space_found = True

                # Look for time complexity
                if not time_found and re.search(r'\btime\b', line, re.IGNORECASE):
                    rightmost_time_idx = line.rfind('O(', 0, line.lower().find('time'))
                    if rightmost_time_idx != -1:
                        time_complexity = re.search(r'O\([^)]*(?:\([^)]*\))*\)', line[rightmost_time_idx:]).group(0).strip()
                        time_found = True
            elif time_found or space_found:
                break

    return time_complexity, space_complexity


# Function to extract problem source link from a file
def extract_problem_link(file_path):
    problem_link = "N/A"

    with open(file_path, 'r') as file:
        for line in file:
            if re.search(r'(link:|source:)', line, re.IGNORECASE):
                match = re.search(r'http[s]?://\S+', line)
                if match:
                    problem_link = match.group(0).strip()
                    break

    return problem_link


# Function to extract domain name from a URL
def extract_domain_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    # Extract only the main domain part, without subdomains
    domain_parts = domain.split('.')
    if len(domain_parts) >= 2:
        return '.'.join(domain_parts[-2:])
    return "N/A"


# Function to read the project description from DESCRIPTION.md
def read_description():
    description_file = 'DESCRIPTION.md'
    if os.path.exists(description_file):
        with open(description_file, 'r') as file:
            return file.read().strip()
    else:
        raise FileNotFoundError(f"Error: {description_file} not found. Please ensure it exists in the project directory.")

# Function to read the project usage instructions from USAGE.md
def read_usage():
    description_file = 'USAGE.md'
    if os.path.exists(description_file):
        with open(description_file, 'r') as file:
            return file.read().strip()
    else:
        raise FileNotFoundError(f"Error: {description_file} not found. Please ensure it exists in the project directory.")

# Function to generate the index for the README.md file
def generate_readme(root_dir):
    project_description = read_description()
    project_usage = read_usage()

    readme_file = os.path.join(root_dir, 'README.md')

    sections = {}
    for folder in os.listdir(root_dir):
        if folder.startswith('.'):
            continue
        folder_path = os.path.join(root_dir, folder)
        if os.path.isdir(folder_path):
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
                            time_complexity, space_complexity = extract_complexity(file_path)

                            # Extract problem source link
                            problem_link = extract_problem_link(file_path)
                            problem_domain = extract_domain_name(problem_link)

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
            if subfolders:
                sections[folder] = subfolders

    with open(readme_file, 'w') as readme:
        readme.write('# Coding-Challenges\n\n')
        readme.write(f'{project_description}\n\n')

        for section in sorted(sections):
            subfolders = sections[section]
            readme.write(f'## {section.capitalize()}\n\n')
            for subfolder in sorted(subfolders):
                problems = subfolders[subfolder]
                readme.write(f'### {subfolder.capitalize()}\n')
                readme.write('| Nr. | Challenge | Time Complexity | Space Complexity | Solution Code | Problem Link |\n')
                readme.write('| --- | --- | --- | --- | --- | --- |\n')
                for problem in problems:
                    if 'N/A' in problem["problem_link"]:
                        problem_md_link = 'N/A'
                    else:
                        problem_md_link = f'[{problem["problem_domain"]}]({problem["problem_link"]})'
                    readme.write(f'| {problem["problem_number"]} | {problem["challenge"]} '
                                 f'| {problem["time"]} | {problem["space"]} '
                                 f'| [{problem["solution_lang"]}]({problem["solution_link"]}) '
                                 f'| {problem_md_link} |\n')
                readme.write('\n')

        readme.write(f'{project_usage}\n\n')

if __name__ == '__main__':
    generate_readme("./")
