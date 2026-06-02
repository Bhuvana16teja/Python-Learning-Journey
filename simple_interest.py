# Given three integers p, r, and t representing:
# p -> Principal amount
# r -> Rate of Interest
# t -> Time period
#
# Calculate and print the Simple Interest.
#
# Formula:
# Simple Interest = (p * r * t) / 100
#
# Example 1:
# Input:
# 100
# 20
# 2
# Output:
# 40.00
#
# Example 2:
# Input:
# 999
# 9
# 9
# Output:
# 809.19

p = int(input())
r = int(input())
t = int(input())

simple_interest = (p * r * t) / 100

print(f"{simple_interest:.2f}")