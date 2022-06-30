# Devsnest Pattern (Strings)
# Return the pattern of sizeM x N with specifications:
# The pattern should have ‘DEVSNEST!’ written in the center.
# The pattern should only use |, . and - characters
# Note: M is an odd natural number, and N is 3 times M

# Input Format
# First Parameter - Integer M
# Second Parameter - Integer N

# Output Format
# Return the array of string

# Example 1
# Input: 
#     9
#     27
# Output:
#     ------------.|.------------
#     ---------.|..|..|.---------
#     ------.|..|..|..|..|.------
#     ---.|..|..|..|..|..|..|.---
#     ---------DEVSNEST!---------
#     ---.|..|..|..|..|..|..|.---
#     ------.|..|..|..|..|.------
#     ---------.|..|..|.---------
#     ------------.|.------------


# Constraints
# 5 < M < 101
# 15 < N < 303
# M is an odd natural number, and N is 3 times M.

# SOLUTION
def solve(M, N):
    res = []
    for i in range(1,M,2):
        res.append("-"*((N-(3*i))//2) + ".|."*i + "-"*((N-(3*i))//2))
    a = list(reversed(res))
    res.append("-"*((N-9)//2) + "DEVSNEST!" + "-"*((N-9)//2))
    res.append(a)
    return res

print(solve(9,27))

#OUTPUT
# ['------------.|.------------', '---------.|..|..|.---------', '------.|..|..|..|..|.------', '---.|..|..|..|..|..|..|.---', '---------DEVSNEST!---------', ['---.|..|..|..|..|..|..|.---', '------.|..|..|..|..|.------', '---------.|..|..|.---------', '------------.|.------------']]
