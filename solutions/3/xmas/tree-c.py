def make_tree(rows, art='*', counter=0):
    rows = rows-1
    counter += 1
    if (rows == -1):
        return
    make_tree(rows, art, counter)
    print(counter*len(art)*' '+(2*rows+1)*art)


make_tree(10)
