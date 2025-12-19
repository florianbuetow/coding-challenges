# O(n log n + n*k) time and O(n) space, n = len(meetings), k = max(len(meeting) for meeting in meetings)
# link: https://leetcode.com/problems/find-all-people-with-secret/

from heapq import heapify, heappop
from collections import defaultdict
from typing import List


class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        knowers = set([0, firstPerson])
        meetings = [[t, p1, p2] for p1, p2, t in meetings]
        heapify(meetings)  # O(n)
        while meetings:  # O(n)
            t = meetings[0][0]
            people = defaultdict(set)
            seed = set()
            while meetings and meetings[0][0] == t:
                _, p1, p2 = heappop(meetings)  # O(log n)
                people[p1].add(p2)
                people[p2].add(p1)
                if p1 in knowers:
                    seed.add(p1)
                if p2 in knowers:
                    seed.add(p2)

            while seed:
                p1 = seed.pop()
                for p2 in list(people[p1]):
                    people[p1].remove(p2)
                    people[p2].remove(p1)
                    if p2 not in knowers:
                        knowers.add(p2)
                        seed.add(p2)

        return list(knowers)
