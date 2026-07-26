# link: https://leetcode.com/problems/maximum-product-of-three-numbers/


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # O(n) time and O(1) space
        largest = []
        smallest = []
        for n in nums:
            largest.append(n)
            largest.sort(reverse=True)
            smallest.append(n)
            smallest.sort()
            if len(largest) > 3:
                largest.pop()
                smallest.pop()
        return max(
            largest[0] * largest[1] * largest[2],
            smallest[0] * smallest[1] * largest[0]
        )
