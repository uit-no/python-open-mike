from time import sleep

def clock_generator():
    # To ensure that the function first starts to yield times when t == 12, we use a timer.
    # When the timer < 12, the for loop continues without yielding anything
    timer = 0
    while True:
        for t in range(1, 25):
            timer += 1
            if timer < 12:
                continue
            if t < 13:
                yield "{} pm".format(t)
            if t > 12:
                yield "{} am".format(t-12)

time = clock_generator()

for t in time:
    print(t)
    sleep(1)
