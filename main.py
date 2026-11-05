year = int(input())

# One boolean expression over `year` goes here.
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

if is_leap:
    print("leap")
else:
    print("not leap")