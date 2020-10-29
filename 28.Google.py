#Çözüm-1
def non_duplicated_int(lst):
    return [i for i in lst if lst.count(i) == 1][0]