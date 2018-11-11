from collections import Counter


def freq_using_dicts(text, num):

    # lowercase entire text
    text_lowercase = text.lower()

    # split text into lines
    lines = text_lowercase.splitlines()

    words = {}
    characters = {}

    for line in lines:
        # remove all special characters
        line_no_special = ''.join([c for c in line if c.isalpha() or c == ' '])

        # split line into words
        for word in line_no_special.split():

            if word in words:
                words[word] += 1
            else:
                # we could simplify using defaultdict
                words[word] = 1

            for character in word:
                if character in characters:
                    characters[character] += 1
                else:
                    characters[character] = 1

    # convert dict to list of tuples
    words_freq = words.items()
    characters_freq = characters.items()

    # sort the lists in descending order
    # based on the second element of each tuple
    words_freq = sorted(words_freq, key=lambda t: t[1], reverse=True)
    characters_freq = sorted(characters_freq, key=lambda t: t[1], reverse=True)

    return words_freq[:num], characters_freq[:num]


def freq_using_counter(text, num):

    # lowercase entire text
    text_lowercase = text.lower()

    # split text into lines
    lines = text_lowercase.splitlines()

    words = []
    characters = []

    for line in lines:
        # remove all special characters
        line_no_special = ''.join([c for c in line if c.isalpha() or c == ' '])

        # split line into words
        for word in line_no_special.split():
            words.append(word)
            for character in word:
                characters.append(character)

    words_freq = Counter(words).most_common(num)
    characters_freq = Counter(characters).most_common(num)

    return words_freq, characters_freq


if __name__ == '__main__':
    with open('poem.txt', 'r') as f:
        text = f.read()

    print('\nusing dicts')
    words_freq, characters_freq = freq_using_dicts(text=text, num=10)
    print(words_freq)
    print(characters_freq)

    print('\nusing counter')
    words_freq, characters_freq = freq_using_counter(text=text, num=10)
    print(words_freq)
    print(characters_freq)
