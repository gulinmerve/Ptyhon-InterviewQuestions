#Solution 1
lst = [9, 11, 8, 5, 7, 10]
maxdif = 0
for i in range(len(lst)):
	for y in range(len(lst)):
		if lst[y]-lst[i] > maxdif and y > i:
			maxdif = lst[y]-lst[i]
print(maxdif)

#Solution2
lst = [1, 6, 19, 59, 30, 60]
def buy_and_sell(lst):
    max_profit = 0
    min_price = lst[0]
    for price in lst:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit
print(buy_and_sell(lst))

#Solution3
lst = [10, 20, 23, 22, 17, 30]
def buy_and_sell(lst):
    max_profit = 0
    for i in range(len(lst)-1):
        for j in range(i+1, len(lst)):
            if lst[j] - lst[i] > max_profit:
                max_profit = lst[j] - lst[i]
    return max_profit
print(buy_and_sell(lst))


now = datetime.now()
# buraya hızı ölçülecek kod satırları ya da fonksiyon gelecek
later = datetime.now()
print((later - now).total_seconds())


# Çözüm-1
def m_profit(prices):
    result = 0
    for i in range(len(prices)-1):
        result = max(result, max(prices[i+1:]) - prices[i])
    return result

# Çözüm-2
def m_profit2(prices):       
    return 0 if len(prices) < 2 else max(0,max([max(prices[i+1:]) - prices[i] for i in range(len(prices)-1)]))


# Çözüm-3
def m_profit3(prices):
    result = 0
    sell = 0
    for i in range(len(prices)-1,-1,-1):
        sell = max(sell, prices[i])
        result = max(result, sell - prices[i])
    return result


