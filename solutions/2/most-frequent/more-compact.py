# source: https://gist.github.com/thomakra/038b2f75df99368082d34b633d30e66b

with open("poem.txt", "r") as f:
    txt = f.read()

# Solution 1
from itertools import islice

unique_characters = set(txt)
without_punctuation = filter(str.isalpha, unique_characters)
counts = [(c, sum(1 for e in txt if e == c)) for c in without_punctuation]
sorted_counts = sorted(counts, key=lambda e: e[1], reverse=True)
most_frequent = list(islice(sorted_counts, 5))
print(most_frequent)

# Solution 2
from collections import Counter

## Count most common characters
print(Counter([c for c in txt if c.isalpha()]).most_common(n=5))

# Count most common words
def remove_punctuation(x):
    return ''.join(c for c in x if c.isalpha())

words = [word.lower() for line in txt.splitlines() for word in line.split()]
without_punctuation = map(remove_punctuation, words)
most_common = Counter(without_punctuation).most_common(n=5)
print(most_common)
