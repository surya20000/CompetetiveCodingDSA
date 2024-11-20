# Question Link:- https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

# Example 1:


# Input: root = [1,7,0,7,-8,null,null]
# Output: 2
# Explanation: 
# Level 1 sum = 1.
# Level 2 sum = 7 + 0 = 7.
# Level 3 sum = 7 + -8 = -1.
# So we return the level with the maximum sum which is level 2.
# Example 2:

# Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
# Output: 2

# Solution 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root.left is None and root.right is None:
            return 1
        def BFS(root):
            q=deque([root])
            maximum=[]
            maximum.append(root.val)
            while q:
                l=len(q)
                value=0
                for i in range(l):
                    tempRoot=q.popleft()
                    if tempRoot.left:
                        q.append(tempRoot.left)
                        value+=tempRoot.left.val
                    if tempRoot.right:
                        q.append(tempRoot.right)
                        value+=tempRoot.right.val
                print(maximum)
                maximum.append(value)
            maximum.pop()
            print(maximum)
            return maximum.index(max(maximum))+1
        return BFS(root)
