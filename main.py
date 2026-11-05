n = int(input())

for row in range(1, n + 1):
    for col in range(1, n + 1):
        (row * col) % 10
        print((row * col) % 10, end="")
    # TODO: add an inner loop over the columns 1..n.
    # Print each cell's digit without ending the line,
    # and let the print() below close the row.
    print()
