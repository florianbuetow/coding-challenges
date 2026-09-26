# link: https://leetcode.com/problems/evaluate-the-bracket-pairs-of-a-string/

class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        # O(n) time and space
        knowledge = {key: value for key, value in knowledge}
        result = []
        tmp = []
        for c in s:
            if c == '(':
                tmp = ['']
            elif c == ')':
                key = ''.join(tmp)
                tmp.clear()
                result.append(knowledge.get(key, '?'))
            elif tmp:
                tmp.append(c)
            else:
                result.append(c)
        result = ''.join(result)
        return result
