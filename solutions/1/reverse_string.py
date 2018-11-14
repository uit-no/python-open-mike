#!/usr/bin/env python3


# Solution 1
def reverse_string(string):
    return string[::-1]

# Solution 2
def reverse_string_2(string):
    return "".join(reversed(string))


# Solution 3
def reverse_string_3(string):
    output = ""
    for char in string:
        output = char + output
    return output


if __name__ == "__main__":
    string = "Hello world!"
    print("{} reversed is: {}".format(string, reverse_string(string)))
    print("{} reversed is: {}".format(string, reverse_string_2(string)))
    print("{} reversed is: {}".format(string, reverse_string_3(string)))
