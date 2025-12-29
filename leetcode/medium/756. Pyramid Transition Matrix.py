# O(6^2n) time and O(n*6^n) space
# link: https://leetcode.com/problems/pyramid-transition-matrix/

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        loopup = defaultdict(list)
        for pattern in allowed:
            loopup[pattern[:2]].append(pattern[2])

        @cache
        def helper(row):
            if len(row) == 1:
                return True

            choices = []
            for a, b in pairwise(row):
                c = loopup.get(a + b)
                if not c: return False
                choices.append(c)

            def build(i, acc):
                if i == len(choices): return helper(acc)
                for ch in choices[i]:
                    if build(i + 1, acc + ch):
                        return True
                return False

            return build(0, "")

        return helper(bottom)
