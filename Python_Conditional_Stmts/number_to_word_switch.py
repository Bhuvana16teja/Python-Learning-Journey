# File: number_to_word_switch.py

# Question:
# Given a number n, use a switch statement to return:
# 1 -> One
# 2 -> Two
# ...
# 9 -> Nine
# Otherwise return "Unknown".
#
# Example:
# Input:
# 10
#
# Output:
# Unknown

n = int(input())

match n:
    case 1:
        result = "One"
    case 2:
        result = "Two"
    case 3:
        result = "Three"
    case 4:
        result = "Four"
    case 5:
        result = "Five"
    case 6:
        result = "Six"
    case 7:
        result = "Seven"
    case 8:
        result = "Eight"
    case 9:
        result = "Nine"
    case _:
        result = "Unknown"

print(result)
