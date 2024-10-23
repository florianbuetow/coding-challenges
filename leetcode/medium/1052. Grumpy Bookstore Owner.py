class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # O(n) time and O(1) space
        result = left = right = 0
        max_grumpy = cur_grumpy = 0
        for right in range(len(customers)):
            if grumpy[right]:
                cur_grumpy += customers[right]
            else:
                result += customers[right]

            while left <= right and (right - left + 1 > minutes or grumpy[left] == 0):
                if grumpy[left]:
                    cur_grumpy -= customers[left]
                left += 1
            max_grumpy = max(max_grumpy, cur_grumpy)

        result += max_grumpy
        return result