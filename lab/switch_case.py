term = int(input())


match term:
    case 1:
        print(term + 1)
    case 2:
        print(term + 2)
    case 3:
        print(term + 3)
    case _:             # default
        print(term + 4)
