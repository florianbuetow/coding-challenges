# O(1) time and O(1) space
# link: https://leetcode.com/problems/next-greater-numerically-balanced-number/

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        MAX_DIGITS = 8
        MAX_VALUE = 10 ** MAX_DIGITS

        def geneerateSeeds():
            # initial seeds balanced numbers with only one digit
            nums = ["1", "22", "333", "4444", "55555", "666666", "7777777", "88888888", "999999999"]

            # compute all combinations of balanced numbers that are also balanced numbers (powerset)
            powerset = [[]]
            for e in nums:
                if len(e) > MAX_DIGITS: continue
                for i in range(len(powerset)):
                    powerset.append(powerset[i] + [e])

            seeds = []
            for s in powerset:
                if not s: continue
                seed = "".join(sorted(s))
                if len(seed) < MAX_DIGITS:
                    seeds.append(int(seed))
            return seeds

        def findClosestToTarget(digits, picked, cur_val, min_target):
            res = float('inf')
            if len(digits) == len(picked):
                if cur_val >= min_target:
                    res = cur_val
            else:
                for i, digit in enumerate(digits):
                    if i in picked: continue
                    picked.add(i)
                    candidate = findClosestToTarget(digits, picked, cur_val * 10 + digit, min_target)
                    res = min(res, candidate)
                    picked.remove(i)
            return res

        seeds = geneerateSeeds()
        result = max(seeds)
        for seed in seeds:
            if result == n + 1: break
            if seed > n:
                result = min(result, seed)
            else:
                seed = int(str(seed)[::-1])
                if seed > n:
                    digits = [int(digit) for digit in str(seed)]
                    candidate = findClosestToTarget(digits, set(), 0, n + 1)
                    if candidate > n:
                        result = min(result, candidate)
        return result
