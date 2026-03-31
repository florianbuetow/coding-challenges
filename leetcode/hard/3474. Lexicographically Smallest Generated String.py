# link: https://leetcode.com/problems/lexicographically-smallest-generated-string/

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        # O(n*m) time and O(n+m) space, n = len(str1), m = len(str2)

        def applyT(i, path):
            for i in range(len(str1)):
                if str1[i] == 'T':
                    for j in range(len(str2)):
                        if path[i+j] and path[i+j] != str2[j]:
                            return False
                        path[i+j] = str2[j]
            return True

        def applyF(i, path):
            tmp = path[:]
            for i in range(len(str1)):
                if str1[i] == 'F':
                    num_empty = num_equal = 0
                    prv_empty = -1
                    for j in range(len(str2)):
                        if not tmp[i + j]:
                            if not path[i + j]:
                                path[i + j] = 'a'
                            num_empty += 1
                            prv_empty = i + j
                        if path[i + j] == str2[j]:
                            num_equal += 1
                    if num_equal == len(str2):
                        if num_empty > 0:
                            path[prv_empty] = 'b'
                        else:
                            return False
            return True

        result = [None] * (len(str1) + len(str2) - 1)
        if not applyT(0, result): return ""
        if not applyF(0, result): return ""
        return "".join(result)
