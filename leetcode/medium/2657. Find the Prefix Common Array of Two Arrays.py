# link: https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # O(n) time and space

        counter = {n: 2 for n in range(1, 1 + len(A))}
        result = []
        for i in range(len(A)):
            counter[A[i]] -= 1
            if counter[A[i]] == 0: del counter[A[i]]
            counter[B[i]] -= 1
            if counter[B[i]] == 0: del counter[B[i]]
            result.append(len(A) - len(counter))
        return result
