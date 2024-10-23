class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # O(n log n) time and O(1) space        
        boxes.sort()

        result = 0
        left, right = 0, len(warehouse) - 1
        left_height = right_height = float('inf')
        while left <= right and boxes:
            left_height = min(left_height, warehouse[left])
            right_height = min(right_height, warehouse[right])
            if max(left_height, right_height) >= boxes.pop():
                if left_height >= right_height:
                    left += 1
                else:
                    right -= 1
                result += 1                                    
        return result