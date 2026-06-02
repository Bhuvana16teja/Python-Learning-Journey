# Given an integer n, write a program to return the last digit of the number.
#
# Example 1:
# Input: 10
# Output: 0
#
# Example 2:
# Input: 9768
# Output: 8

n = int(input())

last_digit = abs(n) % 10

print(last_digit)
