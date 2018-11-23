import time


def clock_generator():
    '''
    Infinite generator that loops through the hours of the day yielding American-style hours.
    This one uses the built-in module datetime to get rid of nasty conversions.
    Output could be made lower-case etc., but for simplicity, I keep it like this.
    '''

    seconds = 0

    while True:
        yield time.strftime('%I %p', time.gmtime(seconds))
        seconds += 3600  # 3600 seconds in one hour (60*60)


my_clock = clock_generator()

for _ in range(28):
    print(next(my_clock))
