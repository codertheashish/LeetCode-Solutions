class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandies=max(candies)
        ans=[]
        for i in candies:
            if(i+extraCandies)>=maxCandies:
                ans.append(True)
            else:
                ans.append(False)
        return ans


       