# O(n*m) time and O(n*m) space, n = len(target), m = len(set(target))
# link: https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/

class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        def helper(left, right):
            if left > right: return 0
            if left >= len(target): return 0
            if left == right: return target[left]

            res = 0
            min_height = target[left]
            for i in range(left, right):
                min_height = min(min_height, target[i])
            res += min_height

            if min_height > 0:
                partition_left = left
                partition_right = left
                while partition_right < right:
                    target[partition_right] -= min_height
                    if target[partition_right] == 0:
                        if partition_left < partition_right:
                            res += helper(partition_left, partition_right)
                        partition_left = partition_right + 1
                    partition_right += 1
                res += helper(partition_left, partition_right)
            return res
        return helper(0, len(target))
