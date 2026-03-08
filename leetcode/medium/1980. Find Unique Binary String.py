# link: https://leetcode.com/problems/find-unique-binary-string/

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # O(n*k) time and space, n = len(nums), k = len(nums[0])
        def buildTrie(arr):
            root = {}
            for n in arr:
                t = root
                for c in n:
                    if c not in t:
                        t[c] = {}
                    t = t[c]
            return root

        def findMissing(t, path):
            if len(t) == 0: return ''
            if len(t) == 1:
                res = path[:]
                if '0' not in t: res.append('0')
                if '1' not in t: res.append('1')
                while len(res) < len(nums[0]):
                    res.append('0')
                return ''.join(res)

            path.append('0')
            res = findMissing(t['0'], path)
            path.pop()
            if res: return res

            path.append('1')
            res = findMissing(t['1'], path)
            path.pop()
            if res: return res

        return findMissing(buildTrie(nums), [])
