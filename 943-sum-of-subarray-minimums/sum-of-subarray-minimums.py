
class Solution(object):
    def sumSubarrayMins(self, arr):
        MOD = 10**9 + 7
        stack = []
        ans = 0

        for i in range(len(arr) + 1):
            while stack and (
                i == len(arr) or arr[stack[-1]] > arr[i]
            ):
                mid = stack.pop()

                left = stack[-1] if stack else -1
                right = i

                count = (mid - left) * (right - mid)

                ans += arr[mid] * count

            stack.append(i)

        return ans % MOD
