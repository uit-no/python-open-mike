---
layout: post
title: "2018-12-17: Generators, iterators, and recursion"
room: "TEO-H1 1.417"
time: "16:00 - 17:30"
author: the organizers
status: past
---

### Room: TEO-H1 1.417, time: 16:00 - 17:30

## Exercises ([contributed solutions](https://github.com/uit-no/python-open-mike/tree/gh-pages/solutions/3))

1. Study what the `enumerate` function does and write your own `my_enumerate` that has the same effect.
2. Write a generator `clock_generator()` which starts at midnight, moves the time by one hour and returns the time in 12-hour format,
   e.g. `11 am` or `3 pm` and we can call it and advance by one hour infinitely many times:
```
>>> my_clock = clock_generator()
>>> print(next(my_clock))
12 am
>>> print(next(my_clock))
1 am
>>> print(next(my_clock))
2 am
>>> print(next(my_clock))
3 am
```
3. Write a generator which returns the next element of this infinite series: 1, 2, 3, 4, 5, 5, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, ...
4. Write a function which draws or prints a snowflake or x-mas tree in text or ASCII art or somehow - use your creativity! Extra points for using recursion.
   More extra points if the size can be given via argument.
