# link: https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # O(n) time and O(1) space
        seen = {}
        for i, n in enumerate(nums):
            if n in seen:
                if abs(i - seen[n]) <= k:
                    return True
            seen[n] = i
        return False
