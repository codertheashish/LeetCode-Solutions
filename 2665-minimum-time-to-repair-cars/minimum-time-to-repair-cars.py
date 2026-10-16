class Solution(object):
    def repairCars(self, ranks, cars):
        left = 1
        right = min(ranks) * cars * cars

        while left < right:
            mid = (left + right) // 2
            repaired = 0

            for rank in ranks:
                repaired += int((mid / rank) ** 0.5)

                if repaired >= cars:
                    break

            if repaired >= cars:
                right = mid
            else:
                left = mid + 1

        return left