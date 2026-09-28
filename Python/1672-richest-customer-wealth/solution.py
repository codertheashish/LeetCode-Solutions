class Solution(object):
    def maximumWealth(self, accounts):
        ans=0
        for account in accounts:
            ans = max(ans,sum(account))
        return ans
        