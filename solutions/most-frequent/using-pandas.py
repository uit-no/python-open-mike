import pandas
import sys


def freq(string):
    # how many words and characters to show?
    if len(sys.argv) == 1:
        num = 10
    else:
        num = int(sys.argv[1])

    # define the most common punctuation marks
    punctuation = ".,:;-_'´`<>!\"#$%&/()=?@*¨^§"

    # get a list of words with punctuations
    words = string.lower().split()

    # get a list of words without any punctuations by split-joining
    for p in punctuation:
        for i, w in enumerate(words):
            if p in w:
                words[i] = ''.join(w.split(p))

    # get string of characters only
    chars = ''.join(words)

    word_count = []
    counted_words = []
    char_count = []
    counted_chars = []

    # now count all unique words in words
    # and collect them
    for w in set(words):
        word_count.append(words.count(w))
        counted_words.append(w)

    # now count all unique characters in chars
    # and collect them
    for c in set(chars):
        char_count.append(chars.count(c))
        counted_chars.append(c)

    # now look for the 'num' highest counts, and
    # extract all words and characters with those counts
    max_word_count = list(reversed(sorted(word_count)))[0:num]
    max_char_count = list(reversed(sorted(char_count)))[0:num]

    sortedwords = []
    for i in max_word_count:
        for w in set(words):
            if i == words.count(w):
                sortedwords.append(w)

    sortedchars = []
    for i in max_char_count:
        for c in set(chars):
            if i == chars.count(c):
                sortedchars.append(c)

    data_w = {"Word": sortedwords[:num],
              "Frequency": max_word_count}

    data_c = {"Character": sortedchars[:num],
              "Frequency": max_char_count}

    return data_w, data_c


with open('poem.txt', 'r') as f:
    poem = f.read()

data_word = freq(poem)[0]
data_char = freq(poem)[1]

print(pandas.DataFrame(data_word))
print("")
print(pandas.DataFrame(data_char))
