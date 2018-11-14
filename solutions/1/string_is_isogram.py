#!/usr/bin/env python3


# Solution 1
def string_is_isogram(string):
    string = string.lower()
    return len(string) == len(set(string))


# Solution 2
def string_is_isogram_2(string):
    string = string.lower()
    chars = []
    for char in string:
        if char in chars:
            return False
        else:
            chars.append(char)
    return True

# Solution 3
def string_is_isogram_3(string):
    string = string.lower()
    chars = [char for char in string if str.isalpha(char)]
    return len(chars) == len(set(chars))


if __name__ == "__main__":
    isogram = "World"
    string = "Hello"
    print("{} is a is a isogram: {}".format(string, string_is_isogram(string)))
    print("{} is a is a isogram: {}".format(isogram, string_is_isogram(isogram)))
    print("{} is a is a isogram: {}".format(string, string_is_isogram_2(string)))
    print("{} is a is a isogram: {}".format(isogram, string_is_isogram_2(isogram)))
    print("{} is a is a isogram: {}".format(string, string_is_isogram_3(string)))
    print("{} is a is a isogram: {}".format(isogram, string_is_isogram_3(isogram)))
