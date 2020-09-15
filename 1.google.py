def addpath(s):
    if s == "":
        return 0
    lst = s.split("\n\t")
    lst.remove('dir')
    prefix = ["dir"]
    result = []
    prevdepth = 1
    for i in range(len(lst)):
        depth = 1
        while lst[i].startswith("\t"):
            depth += 1
            lst[i] = lst[i][1:]
        while depth < prevdepth:
            prefix.pop(-1)
            prevdepth -= 1
        prevdepth = depth
        if lst[i].count(".") == 0:
            prefix.append(lst[i])
            prevdepth += 1
        else:
            result.append("/".join(prefix) + "/" + lst[i])
    return len(max(result, key=lambda path:len(path))) if result != [] else 0
    