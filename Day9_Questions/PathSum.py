# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

# Question Link:- https://leetcode.com/problems/path-sum/description/?envType=study-plan-v2&envId=top-interview-150

# Solution Class

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        if not root.left and not root.right:
            return targetSum == root.val
        
        left_sum = self.hasPathSum(root.left, targetSum - root.val)
        right_sum = self.hasPathSum(root.right, targetSum - root.val)
        
        return left_sum or right_sum