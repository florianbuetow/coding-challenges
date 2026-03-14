# link: https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        # O(2^n) time and O(n) space
        def helper(prev, path):
            nonlocal k
            if len(path) == n:
                k -= 1
                if k == 0:
                    return "".join(path)
            else:
                for curr in 'abc':
                    if curr == prev: continue
                    path.append(curr)
                    res = helper(curr, path)
                    if res: return res
                    path.pop()
            return ''
        return helper('', [])
