#Hash Map Solution

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        collected = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in collected:
                return [collected[diff], idx]
            collected[val] = idx
        return
    

#Brute Force

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]