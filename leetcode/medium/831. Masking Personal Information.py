# O(n) time and space
# link: https://leetcode.com/problems/masking-personal-information/


class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s:
            s = s.lower()
            pos = s.find('@')
            s = [s[0], '*' * 5, s[pos-1:]]
            s = "".join(s)
        else:
            s = list(s)
            tmp = [[]]
            while s:
                c = s.pop()
                if c in '+-() ': continue
                if len(tmp) == 1 and len(tmp[-1]) < 4:
                    pass
                elif len(tmp[-1]) >= 3:
                    tmp.append([])
                if len(tmp) > 1: c = '*'
                tmp[-1].append(c)
            if len(tmp) > 3: tmp[-1].append('+')
            for i in range(len(tmp)):
                tmp[i].reverse()
                tmp[i] = ''.join(tmp[i])
            tmp.reverse()
            s = "-".join(tmp)
        return s
