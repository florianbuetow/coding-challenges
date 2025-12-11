# O(n*m) time and space, n = num lines, m = max(line length)
# link: https://adventofcode.com/2025/day/11

from functools import lru_cache
from collections import deque, defaultdict

class Solution:
    def computeNumberOfConnections(self, filename) -> int:

        def getNextDeviceConnections():
            with open(filename, "r") as fh:
                for line in fh:
                    line = line.strip()
                    if line:
                        source, destinations = line.split(': ')
                        destinations = destinations.split(' ')
                    yield [source, destinations]

        def buildGraph():
            g = defaultdict(set)
            for src, destinations in getNextDeviceConnections():
                g[src] = set(destinations)
            return g

        def count_paths(g, start, target):            
            @lru_cache(None)
            def dfs(curr_device, seen_fft, seen_dac):
                if curr_device == target:
                    return int(seen_fft and seen_dac)
                count = 0
                for next_device in g[curr_device]:
                    count += dfs(
                        next_device,
                        seen_fft or (next_device == "fft"),
                        seen_dac or (next_device == "dac")
                    )
                return count
            return dfs(start, False, False)

        return count_paths(
            buildGraph(), 
            "svr", 
            "out", 
        )


if __name__ == '__main__':
    s = Solution()
    print(s.computeNumberOfConnections('input_0b.txt'))
    print(s.computeNumberOfConnections('input_1.txt'))
