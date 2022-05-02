def knapsackProblem(items, capacity):
    n = len(items)
	if n<=0 or capacity<=0:
		return [0,[]]
	dp = [[0 for j in range(capacity+1)] for i in range(n)]
	weights = [x[1] for x in items]
	profits = [x[0] for x in items]
	result=[]
	for i in range(n):
		dp[i][0] =0 
	for j in range(1,capacity+1):
		if weights[0]<= j:
			dp[0][j] =profits[0]
			
	for i in range(1,n):
		for j in range(1,capacity+1):
			if weights[i]<=j:
				profit1 = dp[i-1][j]
				profit2 = dp[i-1][j-weights[i]] + profits[i]
				dp[i][j] = max(profit1,profit2)
			else:
				dp[i][j]= dp[i-1][j]
	result.append(dp[n-1][capacity])
	included=[]
	totalP = dp[n-1][capacity]
	for i in range(n-1,-1,-1):
		if totalP!= dp[i-1][capacity]:
			included.append(i)
			totalP -=profits[i]
			capacity -= weights[i]
	if totalP>0:
		included.append(0)
	result.append(included)
	return result
