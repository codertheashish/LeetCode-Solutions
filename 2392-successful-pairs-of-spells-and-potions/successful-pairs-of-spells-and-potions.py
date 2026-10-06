class Solution(object):
    def successfulPairs(self, spells, potions, success):
        potions.sort()

        n = len(potions)
        ans = []

        for spell in spells:
            # Minimum potion strength required
            need = (success + spell - 1) // spell

            l = 0
            r = n - 1

            while l <= r:
                mid = (l + r) // 2

                if potions[mid] >= need:
                    r = mid - 1
                else:
                    l = mid + 1

            ans.append(n - l)

        return ans