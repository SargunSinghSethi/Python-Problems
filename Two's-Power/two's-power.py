# Two's Power (Math)
# Given an integer n , return 1(true) if it is a power of two. Otherwise, return 0(false) .
# An integer x is said to be in power of two if and only if there exists an integer i such that 2i == x.
# Try doing it in both recursive and iterative method


# Input Format
# First Parameter -Number n


# Output Format
# Return the number (0 or 1).

# Example 1
# Input: 22
# Output: False
# Explanation: 22 is not power of 2.

# Example 2
# Input: n=1
# Output: True
# Explanation: 2 to power 0 is 1

# Example 3
# Input: n= 64
# Output: True
# Explanation: 2 to power 6 is 64
	
	
# Constraints:
# -231 <= n <= 231-1 - 1


# RECURSION
def solve(n):
    if n % 2 != 0:
        return 0
    if n == 2 or n == 1:
        return 1
    return solve(n/2)
print(solve(65536))

# ITERATIVE
def solve(n):
    while n != 1:
        if n % 2 != 0:
            return 0
        n /= 2
    return 1
print(solve(65536))
# RESULT - 1
