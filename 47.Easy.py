#Solution1
for i in Input:
    if Input.count(i) > len(Input) / 2:
        print(i)
        break

#Solution2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x = set(nums)
        for i in x:
            if nums.count(i) > len(nums)/2:
                return i

def majorityElement(nums):
    return max(set(nums),key=nums.count)

def majorityElement(nums):
    return max(set(nums),key=nums.count)