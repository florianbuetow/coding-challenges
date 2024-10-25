from typing import List


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # O(n * m) time and space, n paths, m path separators
        MARKER = SEPARATOR = '/'

        def build_trie(folder):
            trie = {}
            for f in folder: # O(n)
                t = trie
                for part in f.split(SEPARATOR): # O(m)
                    if MARKER in t: break # a shorter path with the same prefix already exists
                    if part not in t:
                        t[part] = {}
                    t = t[part]
                t.clear()
                t[MARKER] = True
            return trie

        def collect_paths(trie, path, result):
            if MARKER in trie:
                result.append(SEPARATOR.join(path))
            else:
                for elem in trie:
                    path.append(elem)
                    collect_paths(trie[elem], path, result)
                    path.pop()
            return result

        trie = build_trie(folder)
        return collect_paths(trie, [], [])





