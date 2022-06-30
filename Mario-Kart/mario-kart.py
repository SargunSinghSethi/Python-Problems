# Mario Kart (Arrays)
# In a contest of Mario Kart, the score of each player is recorded in the 2D array leaderboard. Each row of the leaderboard contains the player number and their score.
# Return the players with the second lowest score.
# If there are multiple players with same score, return them in non-decreasing order.

# Input Format
# First Parameter - 2D array leaderboard

# Output Format
# Return the array.


# Example 1:
# Input:
#     5 2
#     3 37
#     1 41
#     2 37
#     5 41
#     4 35
# Output:
#     2 3
# Explanation:
#      5 2 is the size of the leaderboard. The second lowest score is 37 and their corresponding players are 2 and 3.


# Example 2:
# Input:
#     7 2
#     1 41
#     3 47
#     6 41
#     4 50
#     7 36
#     2 47
#     5 50
# Output:
#     1 6
# Explanation:
#     7 2 is the size of the leaderboard. The second lowest score is 41 and the corresponding players are 1 and 6.


# Constraints
# 3 <= leaderboard.size <= 50
# Expected Time Complexity: O(n log(n))
# Expected Space Complexity: O(n)

# SOLUTION
def solve(mat):
    l = [mat[i][1] for i in range(len(mat))]
    # l = []
    # for i in range(len(mat)):
    #     l.append(mat[i][1])
    l = list(set(l))
    l.sort()
    temp = l[1]
    l = [mat[i][0] for i in range(len(mat)) if temp == mat[i][1]]
    # l = []
    # for i in range(len(mat)):
    #     if temp == mat[i][1]:
    #         l.append(mat[i][0])
    l.sort()
    return l


mat = [[3, 37], [1, 41], [2, 37], [5, 41], [4, 35]]
print(solve(mat))
# ANSWER - [2, 3]
