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