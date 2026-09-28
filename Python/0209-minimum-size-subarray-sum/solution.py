class Solution(object):
    def minSubArrayLen(self, target, nums):
        n = len(nums)

        # Prefix sum
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]

        ans = n + 1

        for i in range(n):
            need = target + prefix[i]

            # Binary search for first prefix >= need
            l = i + 1
            r = n

            while l <= r:
                mid = (l + r) // 2

                if prefix[mid] >= need:
                    ans = min(ans, mid - i)
                    r = mid - 1
                else:
                    l = mid + 1

        if ans == n + 1:
            return 0

        return ans