# Line 1 of the input is a whole number, line 2 is a decimal number.
whole = int(input())
decimal = float(input())

# TODO: turn the two lines of text into numbers and add them up
total = whole + decimal

print(total) # the sum, as a decimal
print(int(total))   # the same sum with the fraction chopped off toward zero
print(f"{whole} + {decimal} = {total}")   # the report line
