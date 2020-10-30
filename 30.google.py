def sum_set(s,k): 
    base = []   
    lst = [base] 
    for i in range(len(s)): 
        orig = lst[:] 
        new = s[i] 
        for j in range(len(lst)): 
            lst[j] = lst[j] + [new] 
        lst += orig
    answer=[]
    for r in lst:
        if sum(r)==k:
            answer=r
    return answer



from itertools import permutations
def subset(lst, k):
    for i in range(1, len(lst)+1):
        x = [j for j in permutations(lst, i)]
        for p in x:
            if sum(p) == k:
                return p



