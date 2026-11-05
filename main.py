total = 0
number = int(input()) # 1. Grab the first number

while number != 0:     # 2. Keep going as long as it's not 0
    total += number    # 3. Add it to the total
    number = int(input()) # 4. Grab the next number to check

print(total)