# Coding-Challenges

This repository contains a collection of coding problems solved on various platforms, like LeetCode, organized by difficulty or type. Each solution is implemented in Python and includes a breakdown of the time complexity and space complexity. The goal of this repository is to document problem-solving techniques, data structures, and algorithms while providing insights into the performance of each approach.

___Leetcode___ 

The ```./leetcode/``` directory is structured into categories such as "Easy," "Medium," and "Hard" for ease of navigation, with future expansions for more types of challenges. For each problem, you’ll find a detailed solution along with its associated time and space complexities, parsed directly from the solution file.

## Leetcode

### Medium
| Nr. | Challenge | Time Complexity | Space Complexity | Solution Code | Problem Link |
| --- | --- | --- | --- | --- | --- |
| 2641 | Cousins in Binary Tree II | O(n) | O(n) | [python](leetcode/medium/2641.%20Cousins%20in%20Binary%20Tree%20II.py) | [leetcode.com](https://leetcode.com/problems/cousins-in-binary-tree-ii/) |

## Generating the README

The following outlines the steps to build and run the Docker container that generates the `README.md` file using the `generate_readme.py` script.

#### 0. Prerequisites

- Clone this repository.
- Ensure that Docker is installed and running on your system.

#### 1. Make the Bash Script Executable

Run the following command to make the script executable:

```bash
chmod +x ./generate_readme_using_docker.sh
```

#### 2. Build and Run the Docker Container

```bash
./generate_readme_using_docker.sh
```

- This will build the Docker image every time it is run (to avoid caching)
- It will then run the Docker container to execute the `generate_readme.py` script, which generates the `README.md` file and persists it to your local directory.

#### 3. Verify the Output

Once the container execution is finished, you should see the updated `README.md` file in the same directory where you ran the script.

