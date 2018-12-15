def inf_series_gen():
    i = 0
    while True:
        while(i < 5):
            i += 1
            yield i
        while(i >= 1):
            yield i
            i -= 1
