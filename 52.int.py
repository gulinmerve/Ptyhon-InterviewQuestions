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
