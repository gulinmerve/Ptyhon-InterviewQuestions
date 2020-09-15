def find_max2(lst, k):
    return [max(lst[i:i+k]) for i in range(len(lst)- k +1)]