from itertools import cycle


def infinite_series1():
    numbers = [1, 2, 3, 4, 5]
    while True:
        for i in numbers:
            yield i
        numbers.reverse()


def infinite_series2():
    numbers = [1, 2, 3, 4, 5]
    while True:
        for i in numbers:
            yield i
        for i in numbers[::-1]:
            yield i


def infinite_series3(n):
    numbers = range(1, n+1)
    while True:
        for i in numbers:
            yield i
        for i in reversed(numbers):
            yield i


def infinite_series4(n):
    numbers = range(1, n+1)
    return cycle(list(numbers) + list(reversed(numbers)))


my_series1 = infinite_series1()
my_series2 = infinite_series2()
my_series3 = infinite_series3(5)
my_series4 = infinite_series4(5)

for _ in range(20):
    print(next(my_series1),
          next(my_series2),
          next(my_series3),
          next(my_series4))
