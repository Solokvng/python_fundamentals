text = input()
if len(text) < 2:
# TODO: build a new string whose first and last characters are swapped,
# with every character between them left where it is.
# Remember that a very short string has nothing to swap.
  result = text
else:
  result = text[-1] + text[1:-1] + text[0]
print(result)