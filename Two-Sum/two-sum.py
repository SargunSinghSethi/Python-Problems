# Two Sum (Arrays)
# Google, Amazon, Microsoft, Adobe, Morgan Stanley, Walmart, TCS, Oracle, Visa, Bloomberg, Apple, Uber, Expedia, Salesforce, Paypal, Intel, Dell
# Given an array of integers nums of size n and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Note: The pair of integers must be in the order of their position in the array i.e., the smaller index first then comes the larger one.

# Input Format
# First Parameter - number n
# Second Parameter - array of integers nums of size n
# Third Parameter - number target

# Output Format
# Return the pair of indices in an array.


# Example 1:
# Input : 
#    4
#    2 7 11 15
#    9
# Output : 
#     0 1
# Explaination : nums[0] + nums[1] == 9, return 0, 1


# Example 2:
# Input : 
#     3
#     3 2 4
#     6
# Output : 
#      1 2


# Constraints:
# 2 <= N <= 105
# -109 <= arr[i] <= 109
# -2 * 109 <= target <= 2 * 109
# Only one valid answer exists.
# Expected Time complexity: O(n)
# Expected Space complexity: O(1)


from collections import deque
def solve(n, nums, target):
    res = {}
    a = []
    for i, elem in enumerate(nums):
        comp = target - elem
        if comp in res: 
            return [res[comp],i]
            break
        res[elem] = i

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	target = int(input())
	out = solve(n, nums, target)
	print(*out)
