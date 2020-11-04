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

# Çözüm-1
def f_maxsub(nums):
    result = float("-inf")
    if len(nums) < 2:
        try:
            result = max(0,nums[0])
        except:
            result = 0
        else:
            return result
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            result = max(result, sum(nums[i:j]))
    return max(0,result)

# Çözüm-2
def f_maxsub2(nums):
    result = now = float("-inf")        
    for i in nums:
        now = max(now + i, i)
        result = max(result, now)
    return max(result,0)