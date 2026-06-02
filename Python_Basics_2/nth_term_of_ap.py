# Given three integers a, d, and n where:
# a -> First term of the Arithmetic Progression (A.P.)
# d -> Common difference
# n -> Term number
#
# Calculate the nth term of the A.P. using:
# an = a + (n - 1) * d
#
# Example 1:
# Input:
# 5
# 2
# 5
# Output:
# 13
#
# Example 2:
# Input:
# 10
# 10
# 101
# Output:
# 1010

a = int(input())
d = int(input())
n = int(input())

an = a + (n - 1) * d

print(an)
