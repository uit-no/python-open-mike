def totuple(a, b):
    if len(a) != len(b):
        return "Error: Both lists must have the same lengths!"
    t = []
    for i, eli in enumerate(a):
        for j, elj in enumerate(b):
            if i == j:
                t.append((eli, elj))
    return t


list1 = ["This", "is", "a", "test"]
list2 = ["And", "one", "more", "test"]

print(totuple(list1, list2))
