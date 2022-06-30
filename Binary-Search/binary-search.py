# Binary Search
# Adobe, SAP Labs, Goldman Sachs, Bloomberg, Apple, Uber

# Given an array of integers nums which are sorted in ascending order, and an integer target, write a function to search target in nums. 
# If the target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


# Input Format
# First Parameter - number n

# Second Parameter - array of integers nums of size n

# Third Parameter - number target


# Output Format
# Return the number


# Example 1
# Input:
#     6
#     -1 0 3 5 9 12
#     9
# Output:
#     4
# Explanation:
#     Explanation: 9 exists in nums and its index is 4


# Example 2
# Input:
#     6
#     -1 0 3 5 9 12
#     2
# Output:
#     -1
# Explanation:
#     2 does not exist in nums so return -1


# Constraints
# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique, nums is sorted in ascending order.
# Expected Time Complexity: O(log n)
# Expected Space Complexity: O(1)


def solve(n, nums, target):
    high = n-1
    low = 0
    
    while low <= high:
        i = low + ((high - low) // 2)
        if target == nums[i]:
            return i 
        if target > nums[i]:
            low = i + 1
        else:
            high = i - 1
    return -1
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(solve(len(nums),nums,target))
