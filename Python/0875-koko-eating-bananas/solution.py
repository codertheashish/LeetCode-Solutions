class Solution(object):
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left + right) // 2

            hours = 0

            for bananas in piles:
                hours += (bananas + mid - 1) // mid

            if hours <= h:
                right = mid - 1
            else:
                left = mid + 1

        return left