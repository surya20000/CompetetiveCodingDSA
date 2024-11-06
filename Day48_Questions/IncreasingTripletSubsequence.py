# Question Link:- https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

# Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

# Example 1:

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
# Example 2:

# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:

# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

# Solution Class

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        min1 = float('inf')
        min2 = float('inf')
        for n in nums:
            if n <= min1:
                min1 = n  
            elif n <= min2:
                min2 = n  
            else:
                return True
        return False