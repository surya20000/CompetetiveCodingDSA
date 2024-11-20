# Question Link:- https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

# Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

# The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

# Example 1:


# Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
# Output: 3
# Explanation: The paths that sum to 8 are shown.
# Example 2:

# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: 3

# Solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        self.numOfPaths = 0
        self.dfs(root, target)
        return self.numOfPaths
    
    def dfs(self, node, target):
        if node is None:
            return 
        self.test(node, target)
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        
    def test(self, node, target):
        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)