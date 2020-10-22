def median(lst):
    lst.sort()
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 != 0 else (lst[mid] + lst[mid-1]) / 2 
lst = [2, 1, 5, 7, 2, 0, 5]
for i in range(1,len(lst)):
    print(median(lst[:i]))