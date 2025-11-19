# O(m) time and O(n) space, m = number of calls to setCell/resetCell/getValue, n = number of setCell calls
# link: https://leetcode.com/problems/design-spreadsheet/

from collections import defaultdict
class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = defaultdict(int)

    def setCell(self, cell: str, value: int) -> None:
        self.sheet[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.sheet:
            del self.sheet[cell]

    def getValue(self, formula: str) -> int:
        def getValue(expression: str):
            if expression.isnumeric():
                return int(expression)
            return self.sheet[expression]
        cell1, cell2 = formula[1:].split('+')
        return getValue(cell1) + getValue(cell2)


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
