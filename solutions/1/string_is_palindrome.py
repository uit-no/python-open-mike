from reverse_string import reverse_string


# Solution 1
def string_is_palindrome(string):
    string = string.lower()
    return string == reverse_string(string)


# Solution 2
def string_is_palindrome_2(string):
    string = string.lower()
    for a, b in zip(string, reversed(string)):
        if a != b:
            return False
    return True


if __name__ == "__main__":
    palindrome = "kayak"
    string = "words"
    print("{} is a palindrome: {}".format(string, string_is_palindrome(string)))
    print("{} is a palindrome: {}".format(palindrome, string_is_palindrome(palindrome)))
    print("{} is a palindrome: {}".format(string, string_is_palindrome_2(string)))
    print("{} is a palindrome: {}".format(palindrome, string_is_palindrome_2(palindrome)))
    
