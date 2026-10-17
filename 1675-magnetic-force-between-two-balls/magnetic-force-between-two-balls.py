
class Solution(object):
    def maxDistance(self, position, m):
        position.sort()

        left = 1
        right = position[-1] - position[0]
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            count = 1
            last = position[0]

            for i in range(1, len(position)):
                if position[i] - last >= mid:
                    count += 1
                    last = position[i]

            if count >= m:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1

        return ans
