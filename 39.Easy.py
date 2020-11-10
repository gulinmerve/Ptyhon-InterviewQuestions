# Clarification:
# Confused why the returned value is an integer but your answer is an array?
# Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.
# Internally you can think of this:
// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);
// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}


#Çözüm-1
def removeDuplicates(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j] = nums[i]
        i += 1
    return j+1