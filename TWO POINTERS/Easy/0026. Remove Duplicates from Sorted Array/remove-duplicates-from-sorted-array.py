# Two Pointers Solution

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)
    

# The time complexity of this solution is O(n) and the space complexity is O(1)

# Time Complexity Explanation:
# The time complexity of this solution is O(n), where n is the length of the input list nums. The algorithm iterates over the list once using a for loop, comparing each element with its previous element. Since the iteration is performed in a linear manner, the time complexity is proportional to the size of the input.

# Space Complexity Explanation:
# The space complexity of this solution is O(1), which means it uses constant extra space. It modifies the input list in-place without using any additional data structures that grow with the size of the input. The algorithm only requires a few variables (l and r) to track indices and compare elements, so the space usage remains constant regardless of the input size.
    
#----------------------------------------------------------------

# In Place Sorting

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         nums[:] = sorted(set(nums))
#         return len(nums)


# The time complexity of this solution is O(n log n) and the space complexity is O(n).

# Time Complexity Explanation:
# The time complexity of this solution is O(n log n), where n is the length of the input list nums. The algorithm involves three main steps: converting the list to a set (set(nums)), sorting the set (sorted(set(nums))), and assigning the sorted set back to the nums list (nums[:] = sorted(set(nums))).
# Converting the list to a set has a time complexity of O(n) because it iterates over each element in the list. Sorting the set using sorted() has a time complexity of O(n log n), as it involves comparing and rearranging the elements. Assigning the sorted set back to the nums list using nums[:] = also takes O(n) time.
# Since the steps are performed sequentially, the overall time complexity is dominated by the sorting step, resulting in O(n log n) complexity.

# Space Complexity Explanation:
# The space complexity of this solution is O(n) because it creates a set with the unique elements in nums. The set stores the unique elements, which can have a maximum size of n. When the sorted set is assigned back to the nums list, it overwrites the original list, resulting in O(n) space usage. However, it does not use any additional data structures that grow with the input size, so the space complexity is linear with respect to the input size.

#----------------------------------------------------------------

# .pop() using for loop

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         for i in range(len(nums)-1, 0, -1):
#             if nums[i] == nums[i-1]:
#                 nums.pop(i)
#         return len(nums)


# The time complexity of this solution is O(n^2) and the space complexity is O(1).

# Time Complexity Explanation:
# The time complexity of this solution is O(n^2), where n is the length of the input list nums. The reason for this is that the algorithm uses a for loop with a range that starts from len(nums)-1 and decrements by 1 (-1) in each iteration until it reaches 0. This loop iterates over the list in reverse order. For each index i, it checks if nums[i] is equal to the previous element nums[i-1]. If they are equal, it removes the element at index i using nums.pop(i).
# Removing an element from a list using pop() takes O(n) time because it requires shifting all the subsequent elements to fill the gap left by the removed element. In the worst case, if we remove elements multiple times in the loop, the overall time complexity becomes O(n^2).

# Space Complexity Explanation:
# The space complexity of this solution is O(1), which means it uses constant extra space. The algorithm modifies the nums list in-place and does not use any additional data structures that grow with the size of the input. The space usage remains constant regardless of the input size. However, please note that the time complexity is the dominant factor in terms of efficiency for this solution.

#----------------------------------------------------------------

# .pop() using while loop

# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         i = 1
#         while i < len(nums):
#             if nums[i] == nums[i-1]:
#                 nums.pop(i)
#             else:
#                 i += 1
#         return len(nums)


# The time complexity of this solution is O(n) and the space complexity of this solution is O(1).

# Time Complexity Explanation:
# The time complexity of this solution is O(n), where n is the length of the input list nums. The algorithm uses a while loop to iterate over the list. It starts with i = 1, the second element of the list, and continues until i reaches the end of the list (len(nums)).
# Inside the loop, it checks if the current element (nums[i]) is equal to the previous element (nums[i-1]). If they are equal, it removes the current element using nums.pop(i). The pop() operation takes O(n) time because it requires shifting all the subsequent elements to fill the gap left by the removed element.
# However, the key observation here is that the while loop only advances i when the current element is not equal to the previous element. This means that the while loop does not always remove elements, and in the worst-case scenario, no elements are removed. This results in an overall linear time complexity of O(n).

# Space Complexity Explanation:
# The space complexity of this solution is O(1), which means it uses constant extra space. The algorithm modifies the nums list in-place and does not use any additional data structures that grow with the size of the input. The space usage remains constant regardless of the input size.