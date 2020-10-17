from random import choice
def r_int(n, l):
    return choice([i for i in range(n) if i not in l])

    