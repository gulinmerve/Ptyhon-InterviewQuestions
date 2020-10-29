#Çözüm-1
def non_duplicated_int(lst):
    return [i for i in lst if lst.count(i) == 1][0]

#Çözüm-2
def non_duplicated_int1(lst):
    d = {}
    for i in lst:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return list(filter(lambda x: (d[x] == 1), d))[0]

#Çözüm-3, matematiksel işlem ile çözüm.
# Bunu internette gördüm. Pratik bir çözüm.
def non_duplicated_int2(lst):
    return (sum(set(lst)) * 3 - sum(lst)) // 2