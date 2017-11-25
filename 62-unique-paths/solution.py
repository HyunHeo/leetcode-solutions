"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Problem and description courtesy of LeetCode: https://leetcode.com/problems/unique-paths/description/

:type m: int
:type n: int
:rtype: int
"""
def uniquePaths(self, m, n):
    # While calculating line of n, we only care
    # about the last line of values. The other
    # ones above are no longer needed for calculation
    # of lower paths
    nLine = [1 for i in range(n)]

    for i in range(1, m):
        leftPosPaths = 0
        for pos in range(len(nLine)):
            nLine[pos] = nLine[pos] + leftPosPaths
            leftPosPaths = nLine[pos]

    return nLine[n-1]