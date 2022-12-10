# Import the necessary modules
import re
from collections import Counter

# Read the contents of the Bible text file
with open('bible.txt', 'r') as f:
  text = f.read()

# Use a regular expression to extract all the words from the text
words = re.findall(r'\b\w+\b', text)

# Use the Counter class to count the occurrences of each word
counts = Counter(words)

# Print the 10 most common words and their counts
for word, count in counts.most_common(1000):
  print(f'{word}: {count}')

