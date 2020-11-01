def count_num(n, x):
    lst=[]
    for i in range (1,n+1):
        for j in range (1, n+1):
            lst.append(i*j)
    return lst.count(x)

    # 

    import numpy as np
import pandas as pd
def table():
    n = int(input('pls ent.n: '))
    x = int(input('pls ent.x: '))
    df = pd.DataFrame(index = np.arange(1,n+1), columns=np.arange(1,n+1))
    for i in range(1,len(df)+1):
        df.iloc[i-1] = np.arange(1,n+1)*i
    print(f'there is/are "{df[df==x].count().sum()}" x "{x}" in the table')



    #Solution2
    def multi_tables1(n, x):
        count = 0
    for i in range(1, n + 1):
        if x % i == 0 and x / i <= n:
            count += 1
    return count
    #
    def multi_tables2(n, x):
    return sum([1 for i in range(1, n + 1) if x % i == 0 and x / i <= n])