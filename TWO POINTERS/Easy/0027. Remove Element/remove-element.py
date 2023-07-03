# Optimized Solution avoiding unnecessary Swapping

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        n = len(nums)
        while k < n:
            if nums[k] == val:
                nums[k] = nums[n - 1]
                n -= 1
            else:
                k += 1
        return k
    

# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses a while loop to iterate through the array and swap elements to remove the target value. It only swaps elements when necessary, and the loop runs until the pointer k reaches the length n of the modified array. The time complexity is O(n) because the loop iterates through each element once. The space complexity is O(1) because it uses a constant amount of additional space.

#----------------------------------------------------------------

# In-Place Element Removal (Method 1)

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#         return k
    

# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses a for loop to iterate through the array and assigns elements to the position k in the array if they are not equal to the target value. The time complexity is O(n) because the loop iterates through each element once. The space complexity is O(1) because it uses a constant amount of additional space.

#----------------------------------------------------------------

# In-Place Element Removal (Method 2)

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         for i in range(len(nums)):
#             if nums[i] == val:
#                 continue
#             nums[k] = nums[i]
#             k += 1
#         return k
    

# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution is similar to Method 1 but uses a continue statement to skip the swapping step when the element is equal to the target value. The time complexity is O(n) because the loop iterates through each element once. The space complexity is O(1) because it uses a constant amount of additional space.

#----------------------------------------------------------------

# In-Place Element Removal (Method 3)

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         k = 0
#         for i in nums:
#             if i != val:
#                 nums[k] = i
#                 k += 1
#         return k    
    

# The time complexity of this solution is O(n) and the space complexity is O(1)

# Explanation: This solution uses a for loop to iterate through the array and assigns elements to the position k in the array if they are not equal to the target value. The time complexity is O(n) because the loop iterates through each element once. The space complexity is O(1) because it uses a constant amount of additional space.

#----------------------------------------------------------------

# .pop() using for loop

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         for i in range(len(nums)-1,-1,-1):
#             if nums[i] == val:
#                 nums.pop(i)
#         return len(nums)
    

# The time complexity of this solution is O(n^2) and the space complexity is O(1).

# Explanation: This solution uses a for loop to iterate through the array and uses the .pop() method to remove elements equal to the target value. The time complexity is O(n^2) because the .pop() method has a time complexity of O(n), and the loop iterates through the array once for each pop operation. The space complexity is O(1) because it uses a constant amount of additional space.

#----------------------------------------------------------------

# .pop() using while loop

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         i = 0
#         while i < len(nums):
#             if nums[i] == val:
#                 nums.pop(i)
#             else:
#                 i += 1
#         return len(nums)

# The time complexity of this solution is O(n^2) and the space complexity is O(1).

# Explanation: This solution uses a while loop to iterate through the array and uses the .pop() method to remove elements equal to the target value. The time complexity is O(n^2) because the .pop() method has a time complexity of O(n), and the loop iterates through the array once for each pop operation. The space complexity is O(1) because it uses a constant amount of additional space.