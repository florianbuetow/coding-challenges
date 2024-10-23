class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        # O(n) time and O(1) space
        time_taken = 0
        person_k_wants = tickets[k]
        for i, person_i_wants in enumerate(tickets):
            if i < k:
                times_i_before_k = min(person_i_wants, person_k_wants)
                time_taken += times_i_before_k
            elif i == k:
                time_taken += person_k_wants
                person_k_wants -= 1
            elif i > k:
                times_i_after_k = min(person_i_wants, person_k_wants)
                time_taken += times_i_after_k
        return time_taken