# Merge Sorted Array (Arrays)
# You are given two integer arrays arr1 and arr2 which are sorted in a non-decreasing order and 
# there are two numbers m and n which represent the number of elements in arr1 and arr2 respectively.
# Your task is to merge arr1 and arr2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead should be stored inside the array arr1. 
# To achieve this, arr1 has a length of m + n , where the first m elements denote the elements that should be merged, 
# and the last n elements are set to 0 and should be ignored. arr2 has a length of n.


# Input Format
# First Parameter - m , the number of elements in arr1
# Second Parameter - n, the number of elements in arr2
# Third Parameter - integer array arr1 of length (m+n)
# Fourth Parameter - integer array arr2 of length n


# Output Format
# Return the integer array arr1 with elements merged in non-decreasing order.


# Example 1:
# Input: arr1 = [0], m = 0, arr2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note:- That because m = 0, there are no elements in arr1. The 0 is only there to ensure the merge result can fit in arr1.


# Example 2:
# Input: arr1 = [1], m = 1, arr2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].


# Example 3:
# Input: arr1= [1,2,3,0,0,0], m= 3,arr2=[2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] .


# Constraints:
# arr1.length == (m + n)
# arr2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= arr1[i], arr2[j] <= 109


from collections import deque
def solve(m, n, arr1, arr3):
    if m == 0:
        return arr2
    elif n == 0:
        return arr1
    else:
        arr = [0] * (m + n)
        lptr = m - 1
        rptr = n - 1
        arrptr = m + n - 1
        while lptr >= 0 and rptr >= 0:
            if arr1[lptr] > arr2[rptr]:
                arr[arrptr] = arr1[lptr]
                lptr -= 1
            else:
                arr[arrptr] = arr2[rptr]
                rptr -= 1
            arrptr -= 1
        
        while lptr >= 0:
            arr[arrptr] = arr1[lptr]
            lptr -= 1
            arrptr -= 1
        
        while rptr >= 0:
            arr[arrptr] = arr2[rptr]
            rptr -= 1
            arrptr -= 1
        return arr
        
# arr1 = [1,2,3,4,0,0]
# m = 4
# arr2 = [3,4,5,6,7]
# n = 5
# arr1 = solve(m,n,arr1,arr2)
# print(arr1)

if __name__ == '__main__':
	m = int(input())
	n = int(input())
	arr1 = list(map(int, input().split()))
	arr2 = list(map(int, input().split()))
	res = solve(m, n, arr1, arr2)
	print(*res)
