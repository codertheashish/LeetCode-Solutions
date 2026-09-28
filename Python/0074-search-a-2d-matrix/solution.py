class Solution(object):
    def searchMatrix(self, matrix, target):
        rows=len(matrix)
        cols=len(matrix[0])
        l=0
        r=rows*cols-1
        while l<=r:
            mid=(l+r)//2
            i=mid//cols
            j=mid%cols
            if matrix[i][j]==target:
                return True
            elif matrix[i][j]>target:
                r=mid-1
            else:
                l=mid+1
        return False