"""
There are a row of n houses, each house can be painted with one of the
three colors: red, blue or green. The cost of painting each house with 
a certain color is different. You have to paint all the houses such that 
no two adjacent houses have the same color.
The cost of painting each house with a certain color is represented by a 
n x 3 cost matrix. For example, costs[0][0] is the cost of painting house 
0 with color red; costs[1][2] is the cost of painting house 1 with color 
green, and so on... Find the minimum cost to paint all houses.

:type costs: List[List[int]]
:rtype: int
"""
def minCost(self, costs):
	if not costs:
		return 0
	
	lastR = costs[0][0]
	lastB = costs[0][1]
	lastG = costs[0][2]
	
	for i in range(1, len(costs)):
		currR = min(lastB, lastG) + costs[i][0]
		currB = min(lastR, lastG) + costs[i][1]
		currG = min(lastB, lastR) + costs[i][2]
		lastR = currR
		lastB = currB
		lastG = currG
	
	return min(lastR, lastB, lastG)