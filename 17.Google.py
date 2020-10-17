from random import choice
def r_int(n, l):
    return choice([i for i in range(n) if i not in l])
#
def rand_int(lst, n):
    a=int(np.random.choice(range(0,n), 1))
    return a if a not in lst else rand_int(lst, n)