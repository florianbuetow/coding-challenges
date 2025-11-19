# O(n*n) time and O(n) space
# link: https://leetcode.com/problems/avoid-flood-in-the-city/

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        result, dry = [], []
        full_lakes = set()
        lastrain = defaultdict(int)
        for i, lake in enumerate(rains):
            if not lake: # sunshine
                dry.append(i)
                result.append(1)
                continue
            if lake not in full_lakes:
                full_lakes.add(lake)
                lastrain[lake] = i
                result.append(-1)
                continue
            if not dry: return []

            dry_day = -1
            for j in range(len(dry)):
                if dry[j] > lastrain[lake]:
                    dry_day = dry[j]
                    result[dry_day] = lake
                    lastrain[lake] = i
                    dry.pop(j) # O(n)
                    result.append(-1)
                    break
            if dry_day < 0: return []

        return result
