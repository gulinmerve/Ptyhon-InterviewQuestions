def f_subsets(s):
    result = []
    for i in s:
        result += [j.union({i}) for j in result]
        result.append({i})
    return [{}] + sorted(result, key = len)