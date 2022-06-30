# Product Of Sum And Difference (Math)
# You are given two integers, a and b.
# Compute the Sum and Difference of a and b. Return the Product of Sum and Difference.


# Input Format
# First Parameter - Integer a
# Second Parameter - Integer b


# Output Format
# Return the integer.


# Example 1:
# Input:
#     5
#     2
# Output:
#     21
# Explanation:
#     Sum is (5 + 2)  = 7 and Difference is (5 - 2) = 3. The product of Sum and Difference is 21.


# Example 2:
# Input:
#     -14
#     -4
# Output:
#     180
# Explanation:
#     The Sum is -18 and Difference is -10. The product is 180.


# Constraints
# -104 <= a, b <= 104
# Expected Time Complexity: O(1)
# Expected Space Complexity: O(1)

def solve(a, b):
    return (a + b)*(a - b)
  
a = int(input())
b = int(input())
print(solve(a,b))
