class Solution:
    # O(n) time and space, n = number of days
    # link: https://leetcode.com/problems/student-attendance-record-ii/
    def checkRecord(self, n: int) -> int:
        memory =[{} for _ in range(n+1)]
        def helper(n, total_absences, consecutive_lates):
            if total_absences > 1: return 0
            if consecutive_lates > 2: return 0
            if n == 0: return 1
            key = (total_absences, consecutive_lates)
            if key not in memory[n]:
                count = 0
                count += helper(n - 1, total_absences, 0)
                count += helper(n - 1, total_absences + 1, 0)
                count += helper(n - 1, total_absences, consecutive_lates + 1)
                memory[n][key] = count % 1000000007
            return memory[n][key]
        return helper(n, 0, 0)