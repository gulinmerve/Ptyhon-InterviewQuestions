def compute_itenary(lst, start):
    r = [[i] for i in lst if i[0] == start]
    for _ in range(len(lst)-1):
        r = [i + [j] for i in r for j in lst if (lst.count(j) != i.count(j)) and (i[-1][1] == j[0])]
    r.sort()
    return [i[0] for i in r[0]] + [r[0][-1][1]] if r else None