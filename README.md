# Coding-Challenges

This repository contains a collection of coding problems solved on various platforms, like LeetCode, organized by difficulty or type. Each solution is implemented in Python and includes a breakdown of the time complexity and space complexity. The goal of this repository is to document problem-solving techniques, data structures, and algorithms while providing insights into the performance of each approach.

___Leetcode___ 

The ```./leetcode/``` directory is structured into categories such as "Easy," "Medium," and "Hard" for ease of navigation, with future expansions for more types of challenges. For each problem, you’ll find a detailed solution along with its associated time and space complexities, parsed directly from the solution file.

## Leetcode

### Easy
| Nr. | Challenge | Time Complexity | Space Complexity | Solution Code | Problem Link |
| --- | --- | --- | --- | --- | --- |
| 21 | Merge Two Sorted Lists | O(n) | O(1) | [python](leetcode/easy/21.%20Merge%20Two%20Sorted%20Lists.py) | N/A |
| 234 | Palindrome Linked List | O(n) | O(1) | [python](leetcode/easy/234.%20Palindrome%20Linked%20List.py) | N/A |
| 404 | Sum of Left Leaves | O(n) | O(n) | [python](leetcode/easy/404.%20Sum%20of%20Left%20Leaves.py) | N/A |
| 463 | Island Perimeter | O(n * m) | O(1) | [python](leetcode/easy/463.%20Island%20Perimeter.py) | N/A |
| 876 | Middle of the Linked List | O(n) | O(1) | [python](leetcode/easy/876.%20Middle%20of%20the%20Linked%20List.py) | N/A |
| 1002 | Find Common Characters | O(n) | O(n) | [python](leetcode/easy/1002.%20Find%20Common%20Characters.py) | N/A |
| 1137 | N-th Tribonacci Number | O(n) | O(1) | [python](leetcode/easy/1137.%20N-th%20Tribonacci%20Number.py) | N/A |
| 1380 | Lucky Numbers in a Matrix | O(n*m) | O(n*m) | [python](leetcode/easy/1380.%20Lucky%20Numbers%20in%20a%20Matrix.py) | N/A |
| 1469 | Find All The Lonely Nodes | O(n) | O(h) | [python](leetcode/easy/1469.%20Find%20All%20The%20Lonely%20Nodes.py) | N/A |
| 1598 | Crawler Log Folder | O(n) | O(n) | [python](leetcode/easy/1598.%20Crawler%20Log%20Folder.py) | N/A |
| 1608 | Special Array With X Elements Greater Than or Equal X | O(n) | O(n) | [python](leetcode/easy/1608.%20Special%20Array%20With%20X%20Elements%20Greater%20Than%20or%20Equal%20X.py) | N/A |
| 1791 | Find Center of Star Graph | O(1) | O(1) | [python](leetcode/easy/1791.%20Find%20Center%20of%20Star%20Graph.py) | N/A |
| 1863 | Sum of All Subset XOR Totals | O(n^2) | O(n) | [python](leetcode/easy/1863.%20Sum%20of%20All%20Subset%20XOR%20Totals.py) | N/A |
| 2073 | Time Needed to Buy Tickets | O(n) | O(1) | [python](leetcode/easy/2073.%20Time%20Needed%20to%20Buy%20Tickets.py) | N/A |
| 2331 | Evaluate Boolean Binary Tree | O(n) | O(n) | [python](leetcode/easy/2331.%20Evaluate%20Boolean%20Binary%20Tree.py) | N/A |
| 3063 | Linked List Frequency | O(n) | O(n) | [python](leetcode/easy/3063.%20Linked%20List%20Frequency.py) | N/A |
| 3105 | Longest Strictly Increasing or Strictly Decreasing Subarray | O(n) | O(1) | [python](leetcode/easy/3105.%20Longest%20Strictly%20Increasing%20or%20Strictly%20Decreasing%20Subarray.py) | N/A |
| 3110 | Score of a String | N/A | N/A | [python](leetcode/easy/3110.%20Score%20of%20a%20String.py) | N/A |

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

