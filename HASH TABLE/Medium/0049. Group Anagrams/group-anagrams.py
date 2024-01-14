# HashMap (Method 1: Group by Count/Frequency)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord("a")] += 1

            result[tuple(count)].append(word)

        return result.values() 

# The time complexity of this solution is O(n * k), and the space complexity is also O(n * k).

# Time Complexity Explanation:
# The time complexity of this solution is O(n * k), where n is the number of strings in the input list strs and k is the maximum length of any string in strs. The nested loops involve iterating through each character in each word to calculate the character frequency.

# Space Complexity Explanation:
# The space complexity is O(n * k) as well, where n is the number of strings in the input list (strs), and k is the maximum length of any string in the list. The space complexity is influenced by the storage of the count array for each word.
    
#----------------------------------------------------------------

# HashMap (Method 2: Group by Sorting)

# class Solution:
#     def groupAnagrams(self, strs):
#         result = defaultdict(list)
        
#         for word in strs:
#             sorted_word = ''.join(sorted(word))
#             result[sorted_word].append(word)
        
#         return list(result.values())
    
# The time complexity of this solution is O(n * k logk), and the space complexity is O(n * k).

# Time Complexity Explanation:
# The time complexity of this solution is O(n * k log k), where n is the number of strings in the input list strs, k is the maximum length of any string in strs, and k log k accounts for the sorting of each word.

# Space Complexity Explanation:
# The space complexity is O(n * k), where n is the number of strings in the input list (strs), and k is the maximum length of any string in the list. The space complexity is influenced by the storage of the sorted strings.