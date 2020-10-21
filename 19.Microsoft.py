# Çözüm-1. sort ile listeyi sıralamaya izin varsa işler kolaylaşıyor.
def longest(nums):
    nums.sort()
    d = dict()
    for i in nums:
        d[i] = i
        if i-1 in d.keys():
            d[i] = d[i-1]           
    return (lambda y: y[0]-y[1]+1)(max(d.items(), key = lambda x: x[0]-x[1]))