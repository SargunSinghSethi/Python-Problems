# Factorials (Math)
# The factorial of a positive integer n is the product of all positive integers less than or equal to n.
# You’re given a number and you have to calculate it’s factorial.
# Note: Factorial of 1 = 1, Factorial of 0 = 1
# Try doing it in both recursive and iterative method

# Input Format
# First Parameter - Number n

# Output Format
# Return the number

# Example 1:
# Input : 4
# Output : 24

# Constraints
# 0<=n<=10


# Recursive Method
def solve(n):
    if n == 0 or n ==1:
        return 1
    return solve(n-1) * n
print(solve(5))


#Iterative Method
def solve(n):
    if n == 0 or n == 1:
        return 1
    sum = 0
    for i in range(1,n+1):
        if sum == 0:
            sum = 1
        sum *= i
    return sum
print(solve(5))
