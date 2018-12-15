def christmas_tree(n):
    j = n
    # print(" "*n + "**")
    for i in range(n-1):
        if i % 2 == 0:
            print(" "*j + "/" + "¤"*i*2 + "\ ")
        else:
            print(" "*j + "/" + "§"*i*2 + "\ ")
        j = j - 1

    print(" "*2 + (2*n-1)*"-")

    if n >= 10:
        print(" "*n + "| |")
        print(" "*(n-9) + 3*"[+]" + "|_|" + 3*"[+]")
    else:
        print(" "*n + "|_|")


christmas_tree(7)
christmas_tree(15)
