title = input()

# 1. Keep only letters, digits, and spaces, then join them back into a string
clean_text = "".join([char for char in title if char.isalnum() or char.isspace()])

# 2. Lowercase the text and split it into a list of words (this automatically cleans up extra spaces)
words = clean_text.lower().split()

# 3. Join the words together using a single hyphen
slug = "-".join(words)

print(slug)