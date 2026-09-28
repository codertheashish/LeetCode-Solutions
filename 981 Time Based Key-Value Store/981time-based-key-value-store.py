class TimeMap(object):

    def __init__(self):
        self.data = {}

    def set(self, key, value, timestamp):
        if key not in self.data:
            self.data[key] = []

        self.data[key].append((timestamp, value))

    def get(self, key, timestamp):
        if key not in self.data:
            return ""

        arr = self.data[key]

        l = 0
        r = len(arr) - 1
        ans = ""

        while l <= r:
            mid = (l + r) // 2

            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                l = mid + 1
            else:
                r = mid - 1

        return ans