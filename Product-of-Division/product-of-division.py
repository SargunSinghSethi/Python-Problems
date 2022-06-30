# Product Of Division (Math)
# You are given two integers, a and b.
# Let x be the integer division and y be the decimal(float) division of a and b.
# Return the product of x and y.


# Input Format
# First Parameter - Integer a
# Second Parameter - Integer b


# Output Format
# Return the decimal product of integer division x and decimal division y of a and b.


# Example 1:
# Input:
#     21
#     5
# Output:
#     16.8
# Explanation:
#     The int and float value of 21 / 5 is 4 and 4.2 respectively. The product is 16.8


# Example 2:
# Input:
#     11
#     4
# Output:
#     5.5
# Explanation:
#     The integer and float value of (11 / 4) is 2 and 2.75 respectively. The product is 5.5


# Constraints
# Range of a and b is [-104, 104] except 0.
# Expected Time Complexity: O(1)
# Expected Space Complexity: O(1)

# SOLUTION
def solve(a, b):
    return (a//b)*(a/b)
  
a = int(input())
b = int(input())
print(solve(a,b)
