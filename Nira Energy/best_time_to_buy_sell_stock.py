def maxProfit(prices):
    n = len(prices)
    i = 0
    j = 1
    maxp = 0
    while j < n:
        if prices[j] - prices[i] >= 0:
            profit = prices[j] - prices[i]
            j += 1
            maxp = max(profit, maxp)
        else: # this is where you found out (prices[j] < prices[i] so we could buy at day j instead of selling)
            i = j # move the pointer to the new cheapest day found
            j += 1
    return maxp
        
        
prices = [10,1,5,6,7,1]
prices1 = [10,8,7,5,2]
prices2 = [2,1,2,1,0,1,2]

print(maxProfit(prices2))