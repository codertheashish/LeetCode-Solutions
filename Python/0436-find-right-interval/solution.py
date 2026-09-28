class Solution(object):
    def findRightInterval(self, intervals):
        n = len(intervals)

        starts = []

        for i in range(n):
            starts.append((intervals[i][0], i))

        starts.sort()

        ans = [-1] * n

        for i in range(n):
            end = intervals[i][1]

            l = 0
            r = n - 1
            pos = -1

            while l <= r:
                mid = (l + r) // 2

                if starts[mid][0] >= end:
                    pos = starts[mid][1]
                    r = mid - 1
                else:
                    l = mid + 1

            ans[i] = pos

        return ans