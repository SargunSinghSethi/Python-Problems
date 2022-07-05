# Characters Frequency (Arrays)
# Given a string str1, Return the array containing the frequency of each character in the order of their occurrence.

# Input Format
# First Parameter - string str1

# Output Format
# Return the array.


# Example 1:
# Input:
#     arfardarb
# Output:
#     3 3 1 1 1
# Explanation:
#     a is repeated 3 times, followed by r which is repeated 3 times. f, d and b occurs only 1 time. 


# Constraints
# 1 <= n <= 105
# String contains lowercase letters
# Expected Time Complexity: O(n)
# Expected Space Complexity: O(1)


from collections import deque
def solve(str1):
    res = {}
    for ch in str1:
        if ch not in res:
            res[ch] = 1
        else:
            res[ch] += 1
    return res.values()

if __name__ == '__main__':
	str1 = input()
	res = solve(str1)
	print(*res)
