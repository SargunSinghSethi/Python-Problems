# Best Time To Buy And Sell Stock (Arrays)
# Google, Amazon, Microsoft, Adobe, Paytm, Oracle

# You are given an array of prices where prices[i] is the price of a given stock on an ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Input Format
# First Parameter - number n
# Second Parameter - array of integers of size n

# Output Format
# Return the number.


# Example 1:
# Input:
#     6
#     7 1 5 3 6 4
# Output:
#     5
# Explanation:
#     Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#     Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


# Example 2:
# Input:
#     5
#     7 6 4 3 1
# Output:
#     0
# Explanation:
#     In this case, no transactions are done and the max profit = 0.


# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)


from collections import deque
def solve(n, prices):
    min_price = 100000
    max_profit = 0
    for price in prices:
        if max_profit < price - min_price:
            max_profit = price - min_price
        if min_price > price:
            min_price = price
    return max_profit

if __name__ == '__main__':
	n = int(input())
	prices = list(map(int, input().split()))
	num = solve(n, prices)
	print(num)
