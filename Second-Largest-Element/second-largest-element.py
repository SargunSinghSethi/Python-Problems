# Second Largest Element (Arrays)
# Given an arr of size n. Return the second largest element.

# Input Format - First Parameter - number n
# Second Parameter - array arr of characters of size n

# Output Format
# Return the number.

# Example 1:
# Input:
#     6
#     2 1 2 8 7 8
# Output:
#     7
# Explanation:
#     The second largest element is 7.

# Example 2:
# Input:
#     2
#     20 10
# Output:
#     10
# Explanation:
#     The second largest is 10.

# Constraints
# 1 < n <= 105
# -104 <= arr[i] <= 104
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)


def solve(n, arr):
    arr = list(set(arr))
    arr.sort()
    return arr[-2]

arr = [2, 1, 2, 8, 7, 8]
print(len(arr), arr)
