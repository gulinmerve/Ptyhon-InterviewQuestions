# Çözüm 1
data = ["a", "b", "c", "d"]
res=[""]
for i in data:
    res=[j+k for j in res for k in data if k not in j]