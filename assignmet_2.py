import string

# Read the file
with open("sample.txt", "r") as f:
     text = f.read()

# Convert text to lowercase and remove punctuation
text = text.lower().translate(str.maketrans("", "", string.punctuation))

# Split text into words
words = text.split()

# Count word frequencies
freq = {}
for word in words:
    freq[word] = freq.get(word, 0) + 1

# Get user input
n = int(input("Enter minimum frequency: "))

# Filter and sort words by frequency (descending)
result = {word: count for word, count in freq.items() if count >= n}
sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

# Print result
print(f"Word frequencies ≥ {n}:")
for word, count in sorted_result:
    print(f"{word} - {count}")