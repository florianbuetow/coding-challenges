from collections import deque
from heapq import heapify, heappop
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:        
        # O(n log n) time and O(n) space
        # link: https://leetcode.com/problems/reveal-cards-in-increasing-order/
        n = len(deck)
        result = [0] * n 
        heapify(deck) # O(n) time
        q = deque([i for i in range(n)])
        parityFlag = True
        while q: 
            # size of the q halves each round -> for loop runs log n times
            for _ in range(len(q)): 
                index = q.popleft()    
                if parityFlag:
                    result[index] = heappop(deck)
                else:
                    q.append(index)
                parityFlag = not parityFlag         
        return result