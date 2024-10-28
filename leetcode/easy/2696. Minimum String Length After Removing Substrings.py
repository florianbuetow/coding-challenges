class Solution:
    def minLength(self, string: str) -> int:
        # link: https://leetcode.com/problems/minimum-string-length-after-removing-substrings/
        # O(n*n) time and O(n) space
        def remove_substrings(current_string):
            index, remaining_characters = 0, []
            while index < len(current_string):
                if current_string[index:index + 2] == 'AB' or current_string[index:index + 2] == 'CD':
                    index += 2  # Skip the 'AB' or 'CD' substring
                else:
                    remaining_characters.append(current_string[index])
                    index += 1
            return "".join(remaining_characters)

        updated_string, string = string, ""
        while string != updated_string:
            string = updated_string
            updated_string = remove_substrings(string)
        return len(string)
