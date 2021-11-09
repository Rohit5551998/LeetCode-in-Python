from typing import List 
import math

prices = [7,1,5,3,6,4]

def maxProfit(prices: List[int]) -> int:
	buyPrice = math.inf
	profit = 0

	for price in prices:
		if(buyPrice > price):
			buyPrice = price
		else:
			profit = max(profit, price-buyPrice)

	return profit


print(f"The maximum profit that can be earned is {maxProfit(prices)}")