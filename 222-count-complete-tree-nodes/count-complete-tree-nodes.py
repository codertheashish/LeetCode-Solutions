# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0

        def getHeight(node):
            h = 0

            while node:
                h += 1
                node = node.left

            return h

        left = getHeight(root.left)
        right = getHeight(root.right)

        if left == right:
            return (1 << left) + self.countNodes(root.right)
        else:
            return (1 << right) + self.countNodes(root.left)
        