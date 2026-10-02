class Solution(object):
    def findClosestElements(self, arr, k, x):
        l = 0
        r = len(arr) - k

        while l < r:
            mid = (l + r) // 2

            if x - arr[mid] > arr[mid + k] - x:
                l = mid + 1
            else:
                r = mid

        return arr[l:l + k]