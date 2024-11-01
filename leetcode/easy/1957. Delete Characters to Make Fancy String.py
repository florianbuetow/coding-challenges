class Solution:
    def makeFancyString(self, s: str) -> str:
        # O(n) time and space
        # link: https://leetcode.com/problems/delete-characters-to-make-fancy-string/
        result = []
        prv_char = None
        cur_repetitions = 0
        for cur_char in s:
            delete_cur_char = False
            if prv_char:
                if cur_char != prv_char:
                    cur_repetitions = 0
                else:
                    delete_cur_char = cur_repetitions >= 2
            cur_repetitions += 1
            prv_char = cur_char
            if not delete_cur_char:
                result.append(cur_char)
        return "".join(result)
