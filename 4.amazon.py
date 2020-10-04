def find_longest(s, k):
    for i in range(len(s),1,-1):
        for j in range(0,len(s)-i):
            if len(set(s[j:i])) == k:
                return len(s[j:i])
    return None