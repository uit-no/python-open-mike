#!/usr/bin/env python3
from collections import Counter


def strip_special_chars(string):
    return "".join(char for char in string if char.isalpha())


def char_counter(string, number):
    chars = filter(str.isalpha, string)
    return Counter(chars).most_common(number)


def word_counter(string, number):
    words = map(strip_special_chars, string.split())
    return Counter(words).most_common(number)


if __name__ == "__main__":
    file_name = "Dracula"
    with open(file_name) as page:
        lines = page.read().lower()
    print("# Most frequent words:", word_counter(lines, 5))
    print("# Most frequent chars:", char_counter(lines, 5))
