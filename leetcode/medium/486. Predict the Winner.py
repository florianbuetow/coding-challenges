# link: https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        # O(2^n) time and O(n) space

        def helper(player, p1_score, p2_score, left, right):
            if left >= len(nums): return
            if right < 0:  return

            if left == right:
                if player == 0:
                    return p1_score + nums[left] >= p2_score
                return p1_score >= p2_score + nums[left]

            if player == 0:
                left_pick_wins = helper(1 - player, p1_score + nums[left], p2_score, left + 1, right)
                right_pick_wins = helper(1 - player, p1_score + nums[right], p2_score, left, right - 1)
                return left_pick_wins | right_pick_wins

            left_pick_wins = helper(1 - player, p1_score, p2_score + nums[left], left + 1, right)
            right_pick_wins = helper(1 - player, p1_score, p2_score + nums[right], left, right - 1)
            return left_pick_wins & right_pick_wins

        return helper(0, 0, 0, 0, len(nums) - 1)
