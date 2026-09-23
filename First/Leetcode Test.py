# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         for i,item in enumerate(nums):
#             for j in range(i+1,len(nums)):
#                 post = nums[j]
#                 if item + post == target:
#                     return [i,j]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        cache = {}
        for i,item in enumerate(nums):
            cache[item] = i
        for i,item in enumerate(nums):
            other = target - item
            if other in cache and cache[other] != i:
                return[i,cache[other]]


