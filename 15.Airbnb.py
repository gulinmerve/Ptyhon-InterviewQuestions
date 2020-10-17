def ordered_courses(courses):
    c = courses.copy()
    result = []
    while [] in c.values():
        noreq = [k for k,v in c.items() if v == []]
        for i in noreq:        
            result.append(i)
            del c[i]
            c = {k1:[v2 for v2 in v1 if v2 != i] for k1,v1 in c.items()}
    return result if len(c) == 0 else None