class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # O(n) time and O(1) space, n=len(s)
        # Idea: use an array to store the max length of an ideal sequence for each letter from the alphabet
        result = 0
        max_sequence_length = [0] * 26
        for c in s:
            max_sequence_length_ending_in_c = 0
            curr = ord(c) - ord('a')
            for prev in range(len(max_sequence_length)):
                if abs(prev - curr) <= k:
                    max_sequence_length_ending_in_c = max(max_sequence_length[prev], max_sequence_length_ending_in_c)
            max_sequence_length[curr] = max(max_sequence_length[curr], max_sequence_length_ending_in_c + 1)
            result = max(max_sequence_length[curr], result)
        return result