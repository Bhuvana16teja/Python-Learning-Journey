# Question:
# Given two integers n and m, check the relation between them.
# Print:
# "less" if n < m
# "equal" if n == m
# "greater" if n > m
#
# Example:
# Input:
# 4
# 8
#
# Output:
# less

n = int(input())
m = int(input())

if n > m:
    print("greater")
elif n == m:
    print("equal")
else:
    print("less")
