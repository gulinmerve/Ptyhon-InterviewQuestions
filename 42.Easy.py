def last_word(words:str) -> int:
    words_list = words.split()
    if len(words_list) < 2:
        return 0
    else:
        return len(words_list[-1])
print(last_word("World"))

def last_word(words:str) -> int:

# çözüm-1
def lengthOfLastWord(s):
    lst = s.split()
    return len(lst[-1]) if lst else 0

# çözüm-2
def lengthOfLastWord1(s):
    s = s.strip()
    pos = s.rfind(" ")
    return len(s[pos+1:]) if pos>-1 else (len(s) if s else 0)

def lenlast(s):
    return 0 if ' ' not in s else len(s[s.index(' ')+1:])