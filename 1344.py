class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # 30 degree per hour
        # 0.5 minute per minutes
        hour_angle = (hour % 12 ) * 30 + minutes * 0.5
        minutes_angle = minutes * 6 # 360 / 60

        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)
