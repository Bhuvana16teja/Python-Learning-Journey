# File: greatest_of_three_numbers.py

# Question:
# Given three numbers a, b and c, find the greatest number among them.
#
# Example:
# Input:
# 10
# 3
# 2
#
# Output:
# 10

a = int(input())
b = int(input())
c = int(input())

if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)