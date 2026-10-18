
class Solution(object):
    def minSpeedOnTime(self, dist, hour):
        n = len(dist)

        if hour <= n - 1:
            return -1

        target = int(round(hour * 100))

        left = 1
        right = 10**7

        while left < right:
            mid = (left + right) // 2
            time = 0

            for i in range(n - 1):
                time += (dist[i] + mid - 1) // mid

            # Time ko hundredths mein compare karo
            if time * 100 + (dist[-1] * 100 + mid - 1) // mid <= target:
                right = mid
            else:
                left = mid + 1

        return left
