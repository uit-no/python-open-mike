from itertools import cycle


def clock_generator():
    periods = cycle(['am', 'pm'])
    hours = cycle([12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    period = next(periods)
    while True:
        hour = next(hours)
        yield f'{hour} {period}'
        if hour == 11:
            period = next(periods)


my_clock = clock_generator()

for _ in range(28):
    print(next(my_clock))
