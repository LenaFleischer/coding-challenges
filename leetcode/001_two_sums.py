# python3
# ATTEMPT 1: HASHMAP APPROACH 1/23/2023

class Solution:
    # inputs: nums (list of integers), target (integer)
    # output: list of integers
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize an empty hashmap 
        indices = {}       
          
        # for each thing in the list, check if the complement exists in the dictionary 
        for i, item in enumerate(nums): 
            complement = target-item
            if complement in indices:
                # if we get to this step, the complement will exist at index i
                # so we never overwrite something important
                return [i, indices.get(complement)] 
            # add item into dictionary
            indices[item] = i        


