#Solution1
def summ(nums, target):
    for i in nums:
        for j in [n for n in arr if n != i]:
            if i+j==target:
                return sorted([nums.index(i), nums.index(j)])