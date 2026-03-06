# link: https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/

class Solution:
    def reverseByType(self, s: str) -> str:
        # O(n) time and space
        def reverseChars(lst, alphabet):
            left, right = 0, len(lst) - 1
            while left < right:
                cl = lst[left]
                if cl not in alphabet:
                    left += 1
                    continue
                cr = lst[right]
                if cr not in alphabet:
                    right -= 1
                    continue
                lst[left], lst[right] = cr, cl
                left +=1
                right -= 1

        result = list(s)
        reverseChars(result, "abcdefghijklmnopqrstuvwxyz")
        reverseChars(result, "!@#$%^&*()")
        return "".join(result)
