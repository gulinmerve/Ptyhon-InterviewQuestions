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

# çözüm-3
def twoSum4(nums, target):
    d = {}
    for i in range(len(nums)):
        if target-nums[i] in d:
            return [d[target-nums[i]], i]
        d[nums[i]] = i


class Solution(object):
    def twoSum( self, nums, target):
        i= 0
        j = len(nums)-1
        temp = sorted(nums)
        while i<j:
            if temp[i] + temp[j] == target:
                if temp[i] == temp[j]:
                    x = nums.index(temp[i])
                    nums.remove(temp[i])
                    return x,nums.index(temp[j])+1
                else:
                    return nums.index(temp[i]),nums.index(temp[j])
                break
            elif temp[i]+temp[j] > target:
                j-=1
            elif temp[i]+temp[j] < target:
                i+=1    