#Solution1
def summ(nums, target):
    for i in nums:
        for j in [n for n in arr if n != i]:
            if i+j==target:
                return sorted([nums.index(i), nums.index(j)])

# Çözüm-1
def twoSum1(nums, target):
    for i in range(len(nums)):
        if (target-nums[i] in nums) and nums.index(target-nums[i]) != i:
            return [i, nums.index(target-nums[i])]


# Çözüm-2
def twoSum2(nums, target):
    return [[i] + [nums.index(target-nums[i])] for i in range(len(nums)) if (target-nums[i] in nums) and nums.index(target-nums[i]) != i][0]