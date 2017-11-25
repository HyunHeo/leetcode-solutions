"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Problem and description courtesy of LeetCode: https://leetcode.com/problems/climbing-stairs/description/

:type n: int
:rtype: int
"""
def climbStairs(self, steps):
    if steps <= 2:
        return steps

    a = 1 # Step that is 2 steps before current step
    b = 2 # Step that is 1 step before current step
    c = 0 # current step

    for i in range(3, steps+1):
        c = a + b
        a = b
        b = c

    return c
