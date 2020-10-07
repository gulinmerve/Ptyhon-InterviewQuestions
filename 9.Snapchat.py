def fix_overlap(lst):
    lst.sort(key = lambda x:x[0])
    result = [list(lst[0])]
    for i in lst[1:]:
        if i[0] > result[-1][1]:
            result.append(list(i))
        else:
            result[-1][1] = max(result[-1][1], i[1])
    return [tuple(i) for i in result]


    def fix_overlap2(lst):
        lst.sort(key = lambda x:x[0])
    start, end = lst[0]
    result = []
    for i in lst[1:]:
        if i[0] > end:
            result.append((start,end))
            start, end = i
        else:
            end = max(end, i[1])
    result.append((start,end))
    return result