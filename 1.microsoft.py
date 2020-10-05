given array = 3, 10, 2, 1, 20
Output: 3
The longest increasing subsequence is 3, 10, 20
given array = 3, 2
Output: 1
The longest increasing subsequences are {3} and {2}
given array = 50, 3, 10, 7, 40, 80
Output: 4
The longest increasing subsequence is {3, 7, 40, 80}

given array = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
output : 6
Explanation :
    The sequence : [0, 2, 6, 9, 13, 15] or [0, 4, 6, 9, 11, 15] or [0, 4, 6, 9, 13, 15]


data = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
from itertools import combinations
res=[]
for i in range(len(data),0,-1):
    c = list(combinations(data,i))
    for i in c:
        if list(i)==sorted(i):
            res=list(i)
            print(list(i))
            # break
    if res:
        break


def find_longest_sub(lst):
    subs = [ [] for i in lst]
    subs[0] =[lst[0]]
    for i in range(1, len(lst)):
        for j in range(i):
            if (lst[i] > lst[j]) and (len(subs[j]) + 1 > len(subs[i])):
                subs[i] = subs[j].copy()
        subs[i].append(lst[i])
    return len(max(subs,key=len))

def find_longest_sub2(lst):
    stack = [1] * len(lst)
    for i in range(1, len(lst)):
        for j in range(i):
            if lst[i] > lst[j]:
                stack[i] = max(stack[i], stack[j] + 1)
    return max(stack)