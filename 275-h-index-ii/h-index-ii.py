class Solution(object):
    def hIndex(self, citations):
        n = len(citations)

        l = 0
        r = n - 1

        while l <= r:
            mid = (l + r) // 2

            # Number of papers from mid to end
            papers = n - mid

            if citations[mid] >= papers:
                r = mid - 1
            else:
                l = mid + 1

        return n - l