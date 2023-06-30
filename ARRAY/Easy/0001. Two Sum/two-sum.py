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
    
# The time complexity of this solution is O(n), and the space complexity is also O(n).

# Time Complexity Explanation:
# The time complexity of this solution is O(n), where n is the number of elements in the input list nums. This is because the solution loops through the list once, using a single for-loop that iterates through all elements.

# Space Complexity Explanation:
# The space complexity is O(n) as well. This is because the solution uses a dictionary (collected) to store previously encountered values as keys and their corresponding indices as values. In the worst case, when all elements are distinct and no pair is found, the dictionary will contain n entries.
    
#----------------------------------------------------------------

#Brute Force

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


# The time complexity of this solution is O(n^2), and the space complexity is O(1).

# Time Complexity Explanation:
# The solution uses two nested loops: the outer loop iterates from 0 to n-1, and the inner loop iterates from i+1 to n-1, where n is the length of the input list nums. This means that for each element in the list, it compares it with all the subsequent elements. As a result, the number of comparisons grows quadratically with the size of the input list, leading to a time complexity of O(n^2).

# Space Complexity Explanation:
# The space complexity of this solution is O(1) because it does not use any additional data structures that grow with the size of the input. It only uses a constant amount of space to store the indices of the two elements that sum up to the target.