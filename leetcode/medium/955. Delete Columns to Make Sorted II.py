# O(n * m) time and O(n) space
# link: https://leetcode.com/problems/delete-columns-to-make-sorted-ii/

class Solution:

    def minDeletionSize(self, strs: List[str]) -> int:
        result = 0
        skipCols = set()
        n, m = len(strs), len(strs[0])
        for y in range(m):
            deleteRowFlag = tieFlag = False
            skipColsNew = set()
            for x in range(n-1):
                curr_c = strs[x+0][y]
                next_c = strs[x+1][y]
                if x in skipCols: continue
                if curr_c == next_c:
                    tieFlag = True
                elif curr_c < next_c:
                    skipColsNew.add(x)
                else:
                    skipColsNew.clear()
                    deleteRowFlag = True
                    break
            if deleteRowFlag:
                result += 1
            elif not tieFlag:
                break
            skipCols.update(skipColsNew)
        return result
