class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False

        freq = {}

        for i in s:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in t:
            if i not in freq:
                return False
            else:
                freq[i] -= 1

        for i in freq.values():
            if i != 0:
                return False

        return True