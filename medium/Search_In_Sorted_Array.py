# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         max_num = max(nums)
#         max_num_index = nums.index(max_num)

#         list_1 = nums[:max_num_index + 1]
#         list_2 = nums[max_num_index + 1:]
        
#         list_1.extend(list_2)
        
#         # Do binary search on the sorted list
#         l = 0
#         r = len(nums) - 1
#         return self.bs(l,r,target)
        
#     def bs ( l,r,list_1,target):
#         # Base case
#         if l < r:
#             middle_index = (l + r)/2
#             print(middle_index)
#         else:
#             return -1