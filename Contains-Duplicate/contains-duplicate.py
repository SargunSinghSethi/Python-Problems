# Contains Duplicate (Arrays)
# Google, Amazon, Microsoft, Adobe, TCS, Bloomberg, Apple, Uber

# Given an integer array 'nums’, return 1(true) if any value appears at least twice in the array, and return 0(false) if every element is distinct.


# Input Format
# First Parameter - Number n
# Second Parameter - Array of Integer arr


# Output Format
# Return the integer(0 or 1)


# Example 1:
# Input:
#     4
#     1 2 3 1
# Output:
#     1
# Explanation:
#     '1' is repeated two times.


# Example 2:
# Input:
#     4
#     1 2 3 4 
# Output:
#     0
# Explanation:
#     No values are repeated.


# Constraints:
# 1 <= nums.length <= 105
# -10^9 <= nums[i] <= 10^9

def solve(n, arr):
    s = list(set(arr))
    if len(s) < len(arr):
        return 1
    return 0

arr = [1 2 3 1]
print(solve(len(arr),arr))
