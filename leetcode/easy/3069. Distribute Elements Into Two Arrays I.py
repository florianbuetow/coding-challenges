# link: https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        # O(n) time and space
        arr1, arr2 = [], []
        for n in nums:
            if not arr1:
                arr1.append(n)
            elif not arr2:
                arr2.append(n)
            elif arr1[-1] > arr2[-1]:
                arr1.append(n)
            else:
                arr2.append(n)
        return arr1 + arr2
