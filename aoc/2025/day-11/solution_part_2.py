# O(n*m) time and O(m) space, n = num lines, m = max(line length)
# link: https://adventofcode.com/2025/day/10

from collections import defaultdict

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

        def dfsHelper(g, device, visited):
            if device in visited: return 0
            if device == 'out': 
                if 'dac' in visited and 'fft' in visited:
                    return 1
                return 0
            visited.add(device)
            num_paths = 0
            for connected_device in g[device]:
                num_paths += dfsHelper(g, connected_device, visited)                
            visited.remove(device)
            return num_paths

        return dfsHelper(buildGraph(), 'svr', set())

if __name__ == '__main__':
    s = Solution()
    print(s.computeNumberOfConnections('input_0.txt'))
    print(s.computeNumberOfConnections('input_1.txt'))


