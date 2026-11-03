
class Solution(object):
    def finalPrices(self, prices):
        stack = []
        ans = prices[:]

        for i in range(len(prices)):
            while stack and prices[stack[-1]] >= prices[i]:
                idx = stack.pop()
                ans[idx] -= prices[i]

            stack.append(i)

        return ans
