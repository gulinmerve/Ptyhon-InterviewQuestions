lst = []
items = [2, 1, 5, 7, 2, 0, 5]
for i in items:
    lst.append(i)
    half = len(lst) // 2
    lst.sort()
    if not len(lst) % 2:
        print((lst[half - 1] + lst[half]) / 2.0)
    else:
        print(lst[half]) 

#
def median(lst):
    lst.sort()
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 != 0 else (lst[mid] + lst[mid-1]) / 2 
lst = [2, 1, 5, 7, 2, 0, 5]
for i in range(1,len(lst)):
    print(median(lst[:i]))