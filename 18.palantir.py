def nexperm(lst):
    i = len(lst)-2
    while i >= 0 and lst[i] >= lst[i+1]:
        i -= 1
    if i >= 0:
        j = len(lst)-1
        while j>0 and lst[j] <= lst[i]:
            j -= 1
        lst[i], lst[j] = lst[j], lst[i]
    lst[i+1:len(lst)] = reversed(lst[i+1:len(lst)])
    return lst


# çözüm 2
from itertools import permutations
def nexperm2(lst):
    perm = sorted(list(permutations(lst)))
    i = perm.index(tuple(lst))
    return perm[i+1] if i < len(perm)-2 else perm[0]