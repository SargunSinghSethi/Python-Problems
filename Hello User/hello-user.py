# Hello User(Strings)

# You are given a String str. Return the String by Concatenating it with String "Hello, " and an exclamation mark at the end “!”.

# Input Format
# First Parameter - String str

# Output Format
# Return a String s

# Example 1:
# Input:
#     "Mac"
# Output:
#     "Hello, Mac!"
# Explanation:
#     Given a String, Mac is Concatenated with string "Hello, " at the beginning and "!" at the end
# Constraints
# 1 <= length of string <= 20
# Expected Time Complexity: O(1)
# Expected Space Complexity: O(1)

def solve(str):
    return "Hello, " + str + "!"


print(solve("Mac"))
