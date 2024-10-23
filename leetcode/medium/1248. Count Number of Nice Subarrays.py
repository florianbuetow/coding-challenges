class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # O(n) time and O(1) space
        def helper(k):
            result = left = counter = 0
            for right in range(len(nums)):
                n = nums[right]
                if n % 2 == 1:
                    counter += 1
                while counter > k:
                    if nums[left] % 2 == 1:
                        counter -= 1
                    left += 1
                result += (right - left + 1)
            return result
        return helper(k) - helper(k-1)