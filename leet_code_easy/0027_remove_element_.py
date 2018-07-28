'''
Given an array nums and a value val, remove all instances of that value in-place 
and return the new length.
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. 
It doesn't matter what you leave beyond the new length.
given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.

'''

from collections import Counter

def removeElement(nums, val):

    if val not in nums:
        return len(nums)
    cnt = Counter(nums)
    [nums.remove(val) for time in range(cnt[val])]
    return len(nums)
    
print(removeElement([1,2,3,4,4], 4))    
