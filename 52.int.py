x = []
y = []
other = []
for i in input:
     if 'b' in list(i):
        x.append(i)
    elif 'n' in list(i):
         y.append(i)
    else:
        other.append(i)
dict = {'x':x , 'y':y , 'other': other}
ang = []
for i in dict.values():
    ang.append(i)
print(sorted(ang,key = len,reverse =True)) 

a = {}
for i in Input:
    x = "".join(sorted(i))
    if x in a:
        a[x].append(i)
    else:
        a[x] = [i]
b=list(a.values())
print(b)


def anagram(lst):
    a,b,c=[], [], []
    for i in lst:
        if sorted(i) not in a:
            a.append(sorted(list(i)))
            b.append([])
    for j in range(len(b)):
        for k in lst:
            if sorted(k)==a[j]: b[j].append(k)
    for m in sorted(b, key=len, reverse=True):
        c.append(sorted(m))
    return c
anagram(["eat", "tea", "tan", "ate", "nat", "bat"])


def groupAnagrams(strs):
    anagrams = {}
    for i in strs:
        item = "".join(sorted(i))
        if item in anagrams:
            anagrams[item].append(i)
        else:
            anagrams[item]=[i]
    return anagrams.values()


     a = []
    for i in input:
        d = []
        for j in range(len(input)):
            if sorted(i) == sorted(input[j]):
                d.append(input[j])
        if d not in a:
            a.append(d)
    print(a)


A=["eat", "tea", "tan", "ate", "nat", "bat"]
C=[]
B=[]
for i in A:
    for j in A:
        if set(i)==set(j):
            C.append(j)
    if not C in B:
        B.append(C)
    C=[]
print(B)


mylist = ["eat", "tea", "tan", "ate", "nat", "bat"]
c =[]
for i in mylist:
    k = []
    for j in mylist:
        if set(i) == set(j):
            k.append(j)
    if sorted(k) not in c:
        c.append(sorted(k))
print(c)