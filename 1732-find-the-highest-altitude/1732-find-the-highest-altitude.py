class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        maxAltitude = currentAltitude = 0
        for altitude in gain:
            currentAltitude += altitude
            maxAltitude = max(maxAltitude, currentAltitude)

        return maxAltitude