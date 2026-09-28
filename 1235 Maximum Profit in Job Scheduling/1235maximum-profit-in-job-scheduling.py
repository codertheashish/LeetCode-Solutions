class Solution(object):
    def jobScheduling(self, startTime, endTime, profit):
        jobs = sorted(zip(startTime, endTime, profit))
        n = len(jobs)

        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            start, end, money = jobs[i]

            # Binary search for next non-overlapping job
            left = i + 1
            right = n

            while left < right:
                mid = (left + right) // 2

                if jobs[mid][0] >= end:
                    right = mid
                else:
                    left = mid + 1

            next_job = left

            take = money + dp[next_job]
            skip = dp[i + 1]

            dp[i] = max(take, skip)

        return dp[0]