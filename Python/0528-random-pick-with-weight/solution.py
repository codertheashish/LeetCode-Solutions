
import random

class Solution(object):

    def __init__(self, w):
        self.prefix = []

        total = 0

        for weight in w:
            total += weight
            self.prefix.append(total)

        self.total = total

    def pickIndex(self):
        target = random.randint(1, self.total)

        l = 0
        r = len(self.prefix) - 1

        while l < r:
            mid = (l + r) // 2

            if self.prefix[mid] < target:
                l = mid + 1
            else:
                r = mid

        return l