class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # O(n) time and O(1) space
        counts = [0, 0, 0]
        for n in nums:
            counts[n] += 1
        index = 0
        for n, count in enumerate(counts):
            for _ in range(count):
                nums[index] = n
                index += 1
