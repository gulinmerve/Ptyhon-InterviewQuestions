
#Solution1-
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if not numRows:
            return []
        lst = [[1]]
        tmp = []
        for i in range(1,numRows):
            tmp.append(1)
            for j in range(len(lst[-1])-1):
                tmp.append( lst[-1][j] + lst[-1][j+1] )
            tmp.append(1)
            lst.append(tmp)
            tmp = []
        return lst
#Solution2
 def generate(numRows): 
    result = [[1]]
    for i in range(1,numRows):
        result.append([1]+[result[-1][j]+result[-1][j+1] for j in range(len(result[-1])-1)]+[1])
    return [] if numRows < 1 else result