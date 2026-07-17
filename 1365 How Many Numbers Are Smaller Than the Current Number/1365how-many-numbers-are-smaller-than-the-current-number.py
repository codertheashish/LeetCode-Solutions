class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
       ans=[]
       for i in nums:
        c=0
        for j in nums:
            if j<i:
                c+=1
        ans.append(c)
       return ans
    
        