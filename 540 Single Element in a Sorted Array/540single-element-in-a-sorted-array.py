class Solution(object):
    def singleNonDuplicate(self, nums):
        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            # Make mid even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                l = mid + 2
            else:
                r = mid

        return nums[l]