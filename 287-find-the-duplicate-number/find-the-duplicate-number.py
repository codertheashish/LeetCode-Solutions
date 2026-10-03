class Solution(object):
    def findDuplicate(self, nums):
        l = 1
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            count = 0

            for num in nums:
                if num <= mid:
                    count += 1

            if count > mid:
                r = mid
            else:
                l = mid + 1

        return l