
class Solution(object):
    def scoreOfParentheses(self, s):
        stack = [0]

        for ch in s:
            if ch == '(':
                stack.append(0)
            else:
                value = stack.pop()
                stack[-1] += max(2 * value, 1)

        return stack[0]

