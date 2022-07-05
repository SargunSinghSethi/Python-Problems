# Unique Element In List Of Pairs (Arrays)
# Givven an array of integers nums of size n. Every element appears twice except for one. Return the element which appears only once.

# Input Format
# First Parameter - number n
# Second Parameter - array of integers nums of size n

# Output Format
# Return the number.


# Example 1
# Input: 
#     7
#     2 5 1 9 2 9 5
# Output:
#     1


# Example 2
# Input:
#     5
#     1 6 6 8 1
# Output:
#     8


# Constraints
# 0 < n < 104
# 0 < arr[i] < 105
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)


from collections import deque
def solve(n, nums):
    elem = 0
    for i in nums:
        elem = elem ^ i
    return elem

if __name__ == '__main__':
	n = int(input())
	nums = list(map(int, input().split()))
	res = solve(n, nums)
	print(res)
 
