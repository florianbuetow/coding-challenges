from typing import List

class FirstUnique:
    # O(n) time and space
    # link: https://leetcode.com/problems/first-unique-number/submissions/
    # idea: keep a pointer to the first unique number and a lookup table to count the number of occurrences of each number. Advance the pointer if the number it points to is no longer unique

    def __init__(self, nums: List[int]): # O(n) time
        self._q = []
        self._count = {}
        self._ptr2uniq = 0
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int: # O(1) time
        if self._ptr2uniq >= len(self._q):
            return -1
        return self._q[self._ptr2uniq]

    def add(self, value: int) -> None: # O(1) time
        self._q.append(value)
        self._count[value] = self._count.get(value, 0) + 1
        self._update_unique()

    def _update_unique(self): # O(1) time, amortized
        while self._ptr2uniq < len(self._q):
            if self._count[self._q[self._ptr2uniq]] > 1:
                self._ptr2uniq += 1
            else:
                break
