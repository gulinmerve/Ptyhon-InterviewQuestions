lst = [9, 11, 8, 5, 7, 10]
maxdif = 0
for i in range(len(lst)):
	for y in range(len(lst)):
		if lst[y]-lst[i] > maxdif and y > i:
			maxdif = lst[y]-lst[i]
print(maxdif)