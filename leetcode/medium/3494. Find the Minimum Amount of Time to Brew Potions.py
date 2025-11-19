# O(n*m) time and O(m) space, m = num wizards = len(skill), n = number of potions = len(mana)
# link: https://leetcode.com/problems/find-the-minimum-amount-of-time-to-brew-potions/

class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        time = [0] * len(skill)
        for m in mana:
            for w, s in enumerate(skill):
                duration = s * m
                if w == 0:
                    time[w] += duration
                else:
                    time[w] = max(time[w-1], time[w]) + duration
            for w in range(len(skill)-2,-1,-1):
                time[w] = time[w+1] - skill[w+1] * m
        return time[-1]
