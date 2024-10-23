class Solution:
    def partition(self, string: str) -> List[List[str]]:
        # O(n*n) time and space

        def isPalindrome(left, right):
            while left < right:
                if string[left] != string[right]: return False
                left, right = left + 1, right - 1
            return True

        cache = {} # O(n*n) space
        def findPalindromePrefixes(left, right):
            key = (left, right)
            if key not in cache:
                cache[key] = []
                for mid in range(left, right):
                    if isPalindrome(left, mid):
                        cache[key].append([left, mid])
                cache[key] = cache[key][::-1]
            return cache[key]


        result = []
        def helper(left, right, path):
            if left >= right:
                result.append(path[:])
            else:
                for _, p_end in findPalindromePrefixes(left, right):
                    path.append(string[left:p_end+1])
                    helper(p_end + 1, right, path)
                    path.pop()
            return result

        return helper(0, len(string), [])
