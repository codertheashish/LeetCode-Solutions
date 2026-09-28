class Solution(object):
    def spiralOrder(self, matrix):
        n = len(matrix)
        m = len(matrix[0])

        ans = []

        rowstart = 0
        rowend = n - 1
        colstart = 0
        colend = m - 1

        while rowstart <= rowend and colstart <= colend:

            # Left -> Right
            for i in range(colstart, colend + 1):
                ans.append(matrix[rowstart][i])
            rowstart += 1

            # Top -> Bottom
            for i in range(rowstart, rowend + 1):
                ans.append(matrix[i][colend])
            colend -= 1

            # Right -> Left
            if rowstart <= rowend:
                for i in range(colend, colstart - 1, -1):
                    ans.append(matrix[rowend][i])
                rowend -= 1

            # Bottom -> Top
            if colstart <= colend:
                for i in range(rowend, rowstart - 1, -1):
                    ans.append(matrix[i][colstart])
                colstart += 1

        return ans