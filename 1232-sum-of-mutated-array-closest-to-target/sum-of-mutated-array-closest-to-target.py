class Solution(object):
    def findBestValue(self, arr, target):
        l = 0
        r = max(arr)

        while l <= r:
            mid = (l + r) // 2

            total = 0

            for num in arr:
                total += min(num, mid)

            if total < target:
                l = mid + 1
            else:
                r = mid - 1

        # Compare l and l-1
        sum1 = sum(min(num, l) for num in arr)
        sum2 = sum(min(num, l - 1) for num in arr)

        if abs(sum1 - target) < abs(sum2 - target):
            return l
        else:
            return l - 1