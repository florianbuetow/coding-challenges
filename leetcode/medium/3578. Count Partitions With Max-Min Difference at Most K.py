# O(n) time and space
# link: https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        result = 0
        memory = [0, 1] + [0] * len(nums)
        max_q, min_q = deque(), deque()
        left = 0
        for right, n in enumerate(nums):
            while min_q and min_q[-1] > n:
                min_q.pop()
            while max_q and max_q[-1] < n:
                max_q.pop()
            min_q.append(n)
            max_q.append(n)
            while max_q[0] - min_q[0] > k:
                left_n = nums[left]
                if max_q[0] == left_n:
                    max_q.popleft()
                if min_q[0] == left_n:
                    min_q.popleft()
                left += 1
            result = (memory[right + 1] - memory[left]) % (10**9 + 7)
            memory[right + 2] = (memory[right + 1] + result) % (10**9 + 7)
        return result
