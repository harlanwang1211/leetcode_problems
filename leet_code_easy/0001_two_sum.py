def twosum(nums, target):
    '''
    Given nums = [2, 7, 11, 15], target = 9
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    '''
    for i in range(len(nums)):
        for p in range(i + 1, len(nums)):
            if nums[i] + nums[p] == target:
                return [i, p]

#print(twosum([2, 7, 11, 15], 9))
#print(twosum([2, 5, 5, 11], 10))
