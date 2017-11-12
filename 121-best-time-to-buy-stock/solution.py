"""
Say you have an array for which the ith element is the price 
of a given stock on day i.

If you were only permitted to complete at most one transaction (ie, buy one and 
sell one share of the stock), design an algorithm to find the maximum profit.

Problem and description courtesy of LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

:type prices: List[int]
:rtype: int
"""
def maxProfit(self, prices):
	if not prices:
		return 0
	
	maxProfit = 0
	currentMin = prices[0]
	
	for price in prices[1:]:
		if price < currentMin:
			currentMin = price
		elif price - currentMin > maxProfit:
			maxProfit = price - currentMin
			
	return maxProfit
        
