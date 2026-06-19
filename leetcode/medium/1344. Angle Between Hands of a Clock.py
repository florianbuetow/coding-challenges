# link: https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # O(1) time and space
        def getHourHandAngle(hour, minutes):
            return 360 * ((hour % 12 + minutes / 60) / 12)

        def getMinuteHandAngle(minutes):
            return 360 * minutes / 60

        alpha = getHourHandAngle(hour, minutes)
        beta = getMinuteHandAngle(minutes)
        alpha, beta = sorted([alpha, beta])
        return min(
            abs(beta - alpha),
            abs(alpha - beta + 360),
        )
