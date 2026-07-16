class Solution(object):
    def countDigits(self, num):
        temp = num
        ans = 0
        while temp > 0:
            r = temp % 10
            if r != 0 and num % r == 0:
                ans += 1
            temp //= 10
        return ans