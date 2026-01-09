# O(n log n) time and O(n) space
# link: https://leetcode.com/problems/sort-integers-by-binary-reflection

class Solution:
    def sortByReflection(self, nums: List[int]) -> List[int]:
        def toReversedBin(n, numbits):
            bits = []
            while n:
                bits.append(str(n % 2))
                n //= 2
            bits = ['0'] * (numbits - len(bits)) + bits
            return ''.join(bits)

        def computeRequiretedBits(n):
            numbits = 0
            while 2 ** numbits - 1 < n:
                numbits += 1
            return numbits

        numbits = computeRequiretedBits(max(nums))
        for i in range(len(nums)):
            n = nums[i]
            nums[i] = (toReversedBin(n, numbits), n)

        nums.sort(key=lambda e:e[1])
        nums.sort(key=lambda e:e[0])

        result = []
        for _, n in nums:
            result.append(n)
        return result
