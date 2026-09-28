class Solution(object):
    def shipWithinDays(self, weights, days):
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2

            current = 0
            d = 1

            for weight in weights:
                if current + weight > mid:
                    d += 1
                    current = weight
                else:
                    current += weight

            if d <= days:
                r = mid - 1
            else:
                l = mid + 1

        return l