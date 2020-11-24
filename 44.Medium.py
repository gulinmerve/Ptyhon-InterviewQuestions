class Solution:
    def climbStairs(self, n: int) -> int:
        lst = [1,2]
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            for i in range(2,n):
                lst.append(lst[-1]+lst[-2])
            return lst[-1]
#solution 2

from math import factorial
def climbStairs(n):
    count=0
    for i in range(n,1,-2):
        count += factorial(i+(n-i)//2) / factorial(i) / factorial((n-i)//2)
    return int(count)    