# link: https://leetcode.com/problems/successful-pairs-of-spells-and-potions/


class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        # O(n) time and O(1) space
        def countSuccessFullPotions(spell):
            count = 0
            left, right = 0, len(potions) - 1
            while left <= right:
                mid = (left + right) // 2
                if potions[mid] * spell >= success:
                    count = len(potions) - mid
                    right = mid - 1
                else:
                    left = mid + 1
            return count

        pairs = []
        potions.sort()
        for spell in spells:
            count = countSuccessFullPotions(spell)
            pairs.append(count)
        return pairs
