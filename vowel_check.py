# File: vowel_check.py

# Question:
# Given a character ch representing an English alphabet,
# determine whether it is a vowel or not.
# Print "true" if it is a vowel, otherwise print "false".
#
# Example:
# Input:
# a
#
# Output:
# true

ch = input().strip()

if ch == "a" or ch == "A":
    print("true")
elif ch == "e" or ch == "E":
    print("true")
elif ch == "i" or ch == "I":
    print("true")
elif ch == "o" or ch == "O":
    print("true")
elif ch == "u" or ch == "U":
    print("true")
else:
    print("false")