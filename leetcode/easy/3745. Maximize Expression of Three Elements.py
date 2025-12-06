# O(n) time and O(1) space
# link: https://leetcode.com/problems/maximize-expression-of-three-elements/

class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        min_one = float('inf')
        max_two = []
        for n in nums:
            min_one = min(min_one, n)
            max_two.append(n)
            max_two.sort(reverse=True)
            if len(max_two) > 2:
                max_two.pop()
        return sum(max_two) - min_one
