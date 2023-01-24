#python 3


# # SOLUTION 1: horizontal iteration (doesnt work for ["ab", "a"] case yet)
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         # common string initialized to the first string
#         common_string = strs[0]
#         # compare the next string, letter by letter, retain what is common
#         for my_str in strs:
#             # if the common string is EVER empty, we can return 
#             if common_string == "":
#                 return common_string
#             new_common = ""
#             for s,c in zip(my_str, common_string):

#                 if s == c: 
#                     new_common += s
#                 else:
#                     common_string = new_common 
#                     break
#         return common_string


## SOLUTION 2: vertical iteration
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        # iterate over length of first string
        for i in range(len(strs[0])):
            for curr_str in strs:
                # if i is out of bounds, return 
                if i == len(curr_str) or strs[0][i] != curr_str[i]:
                    return prefix
            prefix += strs[0][i]
        return prefix

