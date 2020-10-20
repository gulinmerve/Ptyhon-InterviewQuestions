# Çözüm 1
data = ["a", "b", "c", "d"]
res=[""]
for i in data:
    res=[j+k for j in res for k in data if k not in j]

#Çözüm 2
def perm(lst):    
    r = [[]]
    for _ in lst:
        r = [i + [j] for i in r for j in lst if j not in i]
    return r