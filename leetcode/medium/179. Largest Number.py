class Comparator(str):    
    def __lt__(x: str, y: str) -> str:
        return x+y > y+x        

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # O(n log n) time and O(n) space                        
        iterator = map(str, nums)
        result = sorted(iterator, key=Comparator)
        result = ''.join(result)
        return '0' if result.startswith('0') else result        
