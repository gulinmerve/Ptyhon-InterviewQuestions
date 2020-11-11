class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = res = ""
        for i in s:
            if i not in temp:
                temp+=i
                if len(temp) > len(res):
                    res = temp
            else :
                temp = temp[temp.index(i)+1:] + i
        return len(res)

def lengthOfLongestSubstring(s):
    smax, temp = "", ""
    for i in s:
        if i in temp:
            if len(temp) > len(smax):
                smax = temp
            while i in temp:
                temp = temp[1:]
        temp += i
    return max(len(smax),len(temp))