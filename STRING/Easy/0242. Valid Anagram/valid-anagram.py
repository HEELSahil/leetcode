# Method using Array

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord("a")] += 1

        for char in t:
            count[ord(char) - ord("a")] -= 1

        for val in count:
            if val != 0:
                return False
        return True

# The time complexity of this solution is O(n) and the space complexity is O(1)

# Time Complexity Explanation:
# The time complexity of this solution is O(n), where n is the length of the longer string between s and t. This is because we iterate through both strings once.

# Space Complexity Explanation:
# The space complexity of this solution is O(1), because the size of the character set is constant (26 lowercase letters).
    
#----------------------------------------------------------------

# Hashmap Solution (Method 1)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         result = defaultdict(int)

#         for char in s:
#             result[char] += 1

#         for char in t:
#             result[char] -= 1

#         for val in result.values():
#             if val != 0:
#                 return False
#         return True

# The time complexity of this solution is O(n) and the space complexity is also O(n)

# Time Complexity Explanation:
# The time complexity of this solution is O(n), where n is the length of the longer string between s and t. This is because we iterate through both strings once.

# Space Complexity Explanation:
# The space complexity of this solution is O(n), where n is the length of the longer string between s and t. Each character in the strings needs to be stored in the hashmap, and in the worst case, when there are distinct characters in both strings, the space complexity becomes linear.    

#----------------------------------------------------------------

# Sorting Solution

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         str1 = ''.join(sorted(s))
#         str2 = ''.join(sorted(t))

#         if str1 == str2:
#             return True
#         else:
#             return False

# The time complexity of this solution is O(n log n) and the space complexity is O(n)

# Time Complexity Explanation:
# The time complexity of this solution is O(n log n), where n is the length of the longer string between s and t. This is due to the sorting operation.

# Space Complexity Explanation:
# The space complexity of this solution is O(n), where n is the length of the longer string between s and t. This is influenced by the storage of the sorted strings.     