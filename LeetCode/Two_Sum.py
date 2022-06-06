class Solution(object):
    def twoSum(self, nums, target ):
        
        hash_dict = {}
        for each, number in enumerate(nums):
            difference = target - number
            if difference in hash_dict:
                return [hash_dict[difference], each]
            else:
                hash_dict[number] = each
        return [] 
        
    twoSum([2,7,11,15],9)
