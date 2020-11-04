arr = [34, -50, 42, 14, -5, 86]
def subseq(arr):
	i = len(arr)
	temp = 0
	lst = result = []
	while i:
		if sum(arr[:i]) > temp:
			temp = sum(arr[:i])
			lst = arr[:i]
		i-=1
	i = 0
	while i <  len(lst):
		if sum(lst[i:]) >= temp:
			temp = sum(lst[i:])
			result = lst[i:]
		i+=1
	if result == []:
		return 0
	return result
print(subseq(arr))


def max_sum(array):
    temp = 0
    maximum = 0
    for i in range(len(array)):
        for j in range(1, len(array)+1):
            if (j > i):
                if (sum(array[i:j]) > temp):
                    temp = sum(array[i:j])
                    if (temp > maximum):
                        maximum = temp
    return maximum