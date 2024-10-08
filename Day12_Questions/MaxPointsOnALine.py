# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

# Example 1:


# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3
# Example 2:


# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

#Question Link:- https://leetcode.com/problems/max-points-on-a-line/description/?envType=study-plan-v2&envId=top-interview-150

#Solution Class

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 1: return 1
        res = 2
        for i in range(n):
            d = defaultdict(int)
            for j in range(n):
                if i != j:
                    d[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1
            res = max(res, max(d.values()) + 1)
        return res