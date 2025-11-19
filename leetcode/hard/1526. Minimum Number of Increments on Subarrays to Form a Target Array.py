# O(n) time and O(1) space
# link: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        result = target[0]
        for i in range(1, len(target)):
            if target[i] > target[i-1]:
                result += target[i] - target[i-1]
        return result
