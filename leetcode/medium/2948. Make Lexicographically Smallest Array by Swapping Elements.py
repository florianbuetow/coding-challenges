# link: https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/

class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        # O(n log n) time and O(n) space

        def sortHelper(left, right, arr):
            values = [arr[idx][0] for idx in range(left, right)]
            positions = [arr[idx][1] for idx in range(left, right)]
            positions.sort()
            for pos, val in zip(positions, values):
                nums[pos] = val

        arr = [[val, pos] for pos, val in enumerate(nums)]
        arr.sort(key=lambda e:e[1])
        arr.sort(key=lambda e:e[0])

        left = 0
        for right in range(len(arr)):
            if right > left:
                if abs(arr[right-1][0] - arr[right][0]) > limit:
                    sortHelper(left, right, arr)
                    left = right

        sortHelper(left, len(arr), arr)
        return nums
