---
layout: default
title: Python "open mike" events at UiT
---

## Format

Eventually it could be a platform where participants show something useful to
others. But it will take some time to warm up and until then each event will
have a theme and we will suggest exercises. Participants can prepare these
exercises but do not have to.  We go through the exercise and solutions
together but those who have solved the exercises can present alternative
solutions which we discuss together.

At each event we fix the dates for the next event and together we choose a
theme.


## What to expect

- Informal events.
- Interaction.
- Questions, answers, and discussions.


## What not to expect

Do not expect a semester-long course or lecture series
where you can sit back and somebody presents some slides. The goal is
to discuss, ask questions, and to demo. There are no slides, and there is no lecture.


## Next event: 2018-12-17, 16:00-17:30 in TEO-H1 1.417

Theme: Generators, iterators, and recursion (sorry, we will do context managers some other time)

You can email solutions to Radovan Bast (firstname.lastname@uit.no) who will collect them
and make them available here (without names) so that you can compare.

Exercises (OK to prepare all or prepare none):

1. Study what the `enumerate` function does and write your own `my_enumerate` that has the same effect.
2. Write a function `my_clock` which starts at midnight, moves the time by one hour and returns the time in 12-hour format,
   e.g. `11 am` or `3 pm` and we can call it and advance by one hour infinitely many times.
3. Write a function which returns the next element of this infinite series: 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, ...
4. Write a function which draws or prints a snowflake or x-mas tree in text or ASCII art or somehow - use your creativity! Extra points for using recursion.
   More extra points if the size can be given via argument.


## Past events

### 2018-11-14

Theme: Lists, list comprehensions, dictionaries, sets, and tuples.

You can email solutions to Radovan Bast (firstname.lastname@uit.no) who will collect them
and make them available here (without names) so that you can compare.

Exercises (OK to prepare all or prepare none;
[contributed solutions](https://github.com/uit-no/python-open-mike/tree/gh-pages/solutions/2)):

1. Create a list `a` containing (floating point) numbers. Now create a new list `b` with each element of `a` squared.
2. Combine two lists `[a1, a2, ...]` and `[b1, b2, ...]` to a list of tuples: `[(a1, b1), (a2, b2), ...]`
3. Take some text (can be few paragraphs) from [Project Gutenberg](http://www.gutenberg.org) and find the 5 most
   frequent characters and 5 most frequent words. Ignore all punctuation and we recommend to lowercase the entire text.
4. Consider the following animal observations:

```python
observations = {
    'forest': ['cow', 'cow', 'sheep', 'sheep', 'pig', 'sheep'],
    'plains': ['horse', 'horse', 'sheep', 'horse'],
    'jungle': ['ocelot', 'parrot', 'sheep', 'parrot'],
}
```

Try to answer with code:
- How many distinct species were observed in each biome?
- How many sheep were observed in total?
- Are there any species that appear in all biomes?
- Which animals are only found in the jungle?
- Which is the most common animal of all?
- Are parrots found only in the jungle?


### 2018-10-24

Theme: Strings and lists and looping over lists.

Exercises (OK to prepare all or prepare none):

1. Write a function to reverse a string (e.g. it should turn "stressed" into "desserts").
2. Find out whether a word or sentence is an [isogram](https://en.wikipedia.org/wiki/Isogram).
3. Find out whether a word or sentence is a palindrome.

### 2018-09-27

General discussion about the format, duration, frequency, and topics for the meet-up series.


## Recommended reading

- [Real Python Tutorials](https://realpython.com)
- [The Hitchhiker’s Guide to Python!](https://docs.python-guide.org)
- [Python 3 Module of the Week](https://pymotw.com/3/)


## Topics ideas for future events

- Context managers
- Functional programming
- `collections`
- File I/O
- `pygame`
- `pandas`
- TkInter
