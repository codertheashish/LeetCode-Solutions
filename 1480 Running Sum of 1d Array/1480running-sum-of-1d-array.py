class Solution(object):
    def runningSum(self, nums):
        n=len(nums)
        ans=[]
        ans.append(nums[0])
        for i in range(1,n):
            x=ans[i-1]+nums[i]
            ans.append(x)
        return ans
        