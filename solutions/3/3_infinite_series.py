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


my_series1 = infinite_series1()
my_series2 = infinite_series2()

for _ in range(18):
    print(next(my_series1), next(my_series2))
