# HashMap Solution (Method 1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        collected = {}
        n = len(nums)

        for i in nums:
            if i in collected:
                collected[i] += 1
            else:
                collected[i] = 1
        
        for i, count in collected.items():
            if count > n/2:
                return i
            
# The time complexity of this solution is O(n), and the space complexity is also O(n).

# Time Complexity Explanation:
# The time complexity of this solution is O(n), where n is the size of the input array. This solution uses a dictionary (collected) to store the count of each element. It iterates through the array once, and each dictionary insertion or lookup operation takes O(1) time.
    
# Space Complexity Explanation:
# The space complexity for this solution is also O(n) because, in the worst case, all elements in the array are distinct, and each distinct element requires space in the collected dictionary.

#----------------------------------------------------------------

# HashMap Solution (Method 2)

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         collected = defaultdict(int)
#         n = len(nums)

#         for i in nums:
#             collected[i] += 1
        
#         for i, count in collected.items():
#             if count > n/2:
#                 return i

# The time complexity of this solution is O(n), and the space complexity is also O(n).

# Time Complexity Explanation:
# The time complexity of this solution is O(n), where n is the size of the input array. It iterates through the input array once and performs constant time operations for each element using the collected defaultdict.

# Space Complexity Explanation:
# The space complexity for this solution is also O(n) because, in the worst case, all elements in the array are distinct, and each distinct element requires space in the collected defaultdict.

#----------------------------------------------------------------

# Sorting Solution

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         return nums[n//2]

# The time complexity of this solution is O(n log n), and the space complexity is O(1).

# Time Complexity Explanation:
# The time complexity is O(n log n), where n is the size of the input array. The dominant factor is the sorting step, which takes O(n log n) time using an efficient sorting algorithm.

# Space Complexity Explanation:
# The space complexity is O(1) since the algorithm sorts the array in place without using additional space proportional to the input size.

#----------------------------------------------------------------

# Brute Force (Time Limit Exceeded)

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         for i in nums:
#             count = nums.count(i)
#             if count > n/2:
#                 return i