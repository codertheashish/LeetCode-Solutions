class Solution(object):
    def subtractProductAndSum(self, n):
        temp=n
        sum_=0
        product=1
        while temp>0:
            r=temp%10
            sum_+=r
            product*=r
            temp//=10
        return product-sum_