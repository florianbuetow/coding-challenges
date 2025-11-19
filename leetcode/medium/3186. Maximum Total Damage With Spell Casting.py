# O(n log n) time and O(n) space
# link: https://leetcode.com/problems/maximum-total-damage-with-spell-casting/

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        # counting sort
        damage = {}
        for p in power:
            if p not in damage:
                damage[p] = 0
            damage[p] += p
        damage = [[p, dmg] for p, dmg in damage.items()]
        damage.sort()

        @cache
        def helper(i):
            if i >= len(damage): return 0
            p, dmg = damage[i]
            while i < len(damage) and damage[i][0] <= p + 2:
                i += 1
            return max(
                helper(i+0),
                helper(i+1),
                helper(i+2)
            ) + dmg

        return max(
            helper(0),
            helper(1),
            helper(2)
        )
