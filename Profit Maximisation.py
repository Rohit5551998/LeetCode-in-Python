n = 6

profit_str = "1 2 3 4 9 8"

profit = list(map(int, profit_str.split(" ")))

dp = profit.copy()

for i in range(1, n):
	for j in range(0, i):
		if(profit[i] > profit[j] and profit[i] % profit[j] == 0 and dp[i] < dp[j] + profit[i]):
			dp[i] = dp[j] + profit[i]

print(max(dp))