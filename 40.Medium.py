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