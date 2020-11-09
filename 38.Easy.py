class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        temp = res = ""
        if strs == []:
	        return ""
        for i in range(len(min(strs,key=len))):
            x = strs[0][i]
            for j in strs:
                if j[i]!=x:
                    return res
                else:
                    temp = j[i]
            res += temp
        return res