"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money 
you can rob tonight without alerting the police.

Description courtesy of LeetCode at: https://leetcode.com/problems/house-robber/description/

:type nums: List[int]
:rtype: int
"""
def rob(houses):
		
	if not houses:
		return 0
		
	bestRobsDict = {}
	
	# Allows base cases to be handled without issue
	bestRobsDict[-1] = 0
	bestRobsDict[-2] = 0

	for i in range(len(houses)):
		bestRobsDict[i] = max(bestRobsDict[i-2] + houses[i], bestRobsDict[i-1]) 

	return bestRobsDict[len(houses)-1]
	
	
