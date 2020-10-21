# Çözüm-1. sort ile listeyi sıralamaya izin varsa işler kolaylaşıyor.
def longest(nums):
    nums.sort()
    d = dict()
    for i in nums:
        d[i] = i
        if i-1 in d.keys():
            d[i] = d[i-1]           
    return (lambda y: y[0]-y[1]+1)(max(d.items(), key = lambda x: x[0]-x[1]))


# çözüm-2 listeyi sıralamadan, listenin mevcut hali ile çözüm
def longest2(nums):
    mx = 0
    adj = dict()
    for i in nums:
        if i in adj:
            continue
        lst = [i]*3
        if i - 1 in adj:
            lst[0] = adj[i - 1][0]
        if i + 1 in adj:
            lst[2] = adj[i + 1][1]
        for j in lst:
            adj[j] = lst[0], lst[2]
        mx = max(lst[2] - lst[0] + 1, mx)
    return mx