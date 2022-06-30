# Palindromic Staircase (Math)
# Easy
# Given a Positive Integer n, return an array of string containing the palindromic string of intergers.

# Input Format
# First Parameter - number n

# Output Format
# Return the array of string.

# Example 1:
# Input:
#     5
# Output:
#     1
#     121
#     12321
#     1234321
#     123454321
# Explanation:
#     The size of staircase is 5. So you have to generate string of integers in such a way that it is palindromic. 

# Example 2:
# Input:
#     3
# Output:
#     1
#     121
#     12321

# Constraints
# 0 < n < 10
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(n)

# SOLUTION
def solve(n):
    res = []
    for i in range(1,n+1):
        res.append((((10**i)-1)//9)**2)
    return res
  
print(solve(5))
