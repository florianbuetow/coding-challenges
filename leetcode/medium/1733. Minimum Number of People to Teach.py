# O(n*m + f*k) time and O(n*m) space, n = languages, m = users, f = friendships, k = avg languages per user
# link: https://leetcode.com/problems/minimum-number-of-people-to-teach/

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        know = [set(L) for L in languages]

        candidates = set()
        for u, v in friendships:
            u_idx, v_idx = u - 1, v - 1
            if know[u_idx].isdisjoint(know[v_idx]):
                candidates.add(u_idx)
                candidates.add(v_idx)

        if not candidates:
            return 0

        ans = float('inf')
        for lang in range(1, n + 1):
            to_teach = sum(1 for user in candidates if lang not in know[user])
            if to_teach < ans:
                ans = to_teach

        return ans
