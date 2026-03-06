# link: https://leetcode.com/problems/count-dominant-indices/

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        result = summ = 0
        for i in range(len(nums)-1,-1,-1):
            n = nums[i]
            summ += n
            avg = summ / (len(nums) - i)
            if n > avg:
                result += 1
        return result
