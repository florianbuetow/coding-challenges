# O(1) time and space
# link: https://leetcode.com/problems/binary-watch/


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for hour, minute in itertools.product(range(12), range(60)):
            if hour.bit_count() + minute.bit_count() == turnedOn:
                result.append(f"{hour}:{minute:02d}")
        return result
