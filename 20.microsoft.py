def perm(lst):    
    r = [[]]
    for _ in lst:
        r = [i + [j] for i in r for j in lst if j not in i]
    return r