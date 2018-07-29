# leetcode 0035 Search Insert Position (Easy) 
# https://leetcode.com/problems/search-insert-position/description/

def searchInsert(nums, target):

    if target in nums:
        return nums.index(target) # return the indexx if the target is found
    else:
        nums += [target] # return the index where it would be if it were inserted in order
        nums.sort()
        return nums.index(target)

# test
#print(searchInsert([1,3,5,6],0)) # answer: 0