# link: https://leetcode.com/problems/first-unique-even-element/

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        # O(n) time and space
        counter = defaultdict(int)
        for i, n in enumerate(nums):
            counter[n] += 1
        for i, n in enumerate(nums):
            if n % 2 == 0 and counter[n] == 1:
                return n
        return -1
