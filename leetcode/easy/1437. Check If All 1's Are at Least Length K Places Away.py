class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        # O(n) time and O(1) space
        # link: https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away
        if k == 0: return True # technically not needed
        dist = k
        for n in nums:
            dist += 1
            if n == 1:
                if dist <= k: return False
                dist = 0
        return True
