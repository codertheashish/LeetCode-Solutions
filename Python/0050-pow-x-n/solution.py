class Solution(object):
    def findPow(self, x, n):
        if n==0:
            return 1
        a=self.findPow(x,n//2)
        if n%2==0:
            return a*a
        else:
            return a*a*x
    def myPow(self,x,n):
        if n>=0:
            return self.findPow(x,n)
        else:
            return 1/self.findPow(x,n*(-1))
        