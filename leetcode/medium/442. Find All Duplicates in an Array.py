class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        # O(n) space and time
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1        
        return [n for n, count in counter.items() if count == 2]