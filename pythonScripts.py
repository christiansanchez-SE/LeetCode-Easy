# Two Sums
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
 

# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



# This defines a new class named Solution. In Python, classes are used to create objects that can have attributes (data) and methods (functions)
class Solution(object):
    # This defines a method named twoSum inside the Solution class. The self parameter refers to the instance of the class
        # This method takes three parameters - self: The instance of the class - nums: A list of integers - target: An integer which is the sum we want to find in the list
    def twoSum(self, nums, target): 
        """
        :type nums: List[int] 
        :type target: int
        :rtype: List[int]
        """
        # This initializes an empty dictionary named num_dict. It'll store numbers and their indices
        num_dict = {}

        # This starts a loop that iterates over the nums list. The enumerate function provides both the index (index) and the value (num) of each element in the list
        for index, num in enumerate(nums):
            # For each number in the list, it calculate the complement by subtracting the number (num) from the target. The complement is the number that, when added to num, equals the target
            complement = target - num

            # This checks if the complement is already in the dictionary (num_dict)
            # If it is, it means it have found the two numbers that add up to the target (the current number and its complement)
            # It returns a list containing the indices of these two numbers: the index of the complement (retrieved from the dictionary) and the current index
            if complement in num_dict:
                return [num_dict[complement], index]

            # If the complement is not in the dictionary, we add the current number (num) and its index to the dictionary. This allows us to check for this number as a potential complement in future iterations
            num_dict[num] = index

# Example usage:
    # This creates an instance of the Solution class
solution = Solution()
# This calls the twoSum method on the solution instance, passing in a list of numbers and the target value
# The method returns the indices of the two numbers that add up to the target
print(solution.twoSum([2, 7, 11, 15], 9))  
print(solution.twoSum([3, 2, 4], 6))      
print(solution.twoSum([3, 3], 6))   


# How it works for example one
    # Iteration 1: num = 2, complement = 9 - 2 = 7, num_dict = {2: 0}
    # Iteration 2: num = 7, complement = 9 - 7 = 2 (found in num_dict)
    # Return [0, 1]

# How it works for example two
    # Iteration 1: num = 3, complement = 6 - 3 = 3, num_dict = {3: 0}
    # Iteration 2: num = 2, complement = 6 - 2 = 4, num_dict = {3: 0, 2: 1}
    # Iteration 3: num = 4, complement = 6 - 4 = 2 (found in num_dict)
    # Return [1, 2]

# How it works for example three
    # Iteration 1: num = 3, complement = 6 - 3 = 3, num_dict = {3: 0}
    # Iteration 2: num = 3, complement = 6 - 3 = 3 (found in num_dict)
    # Return [0, 1]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# 2. Palindrome Number

# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -2^31 <= x <= 2^31 - 1
 

# Follow up: Could you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Step 1: Check if the number is negative : If a number is negative, it's not a palindrome. For example, -121 is not the same when read backward because it would be 121- : For positive numbers, we need to reverse the digits of the number and compare it with the original number. If they are the same, the number is a palindrome
        if x < 0:
            return False  # Negative numbers are not palindromes
        
        # Step 2: Store the original number
        original = x
        
        # Step 3: Reverse the digits of the number
        reversed_num = 0
        while x != 0:
            last_digit = x % 10        # Extract the last digit
            reversed_num = reversed_num * 10 + last_digit  # Add it to the reversed number
            x //= 10  # Remove the last digit from x
        
        # Step 4: Compare the original and reversed numbers
        return original == reversed_num  # Return True if they are the same, else False

# Example usage
sol = Solution()
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121)) # Output: False
print(sol.isPalindrome(10))   # Output: False

# Example 1: x = 121
# Initial number: 121
# Reverse process:
# Last digit: 1, Reversed number: 1, Remaining number: 12
# Last digit: 2, Reversed number: 12, Remaining number: 1
# Last digit: 1, Reversed number: 121, Remaining number: 0
# Reversed number is 121, which is the same as the original. So, 121 is a palindrome

# Example 2: x = -121
# The number is negative. Immediately return False

# Example 3: x = 10
# Initial number: 10
# Reverse process:
# Last digit: 0, Reversed number: 0, Remaining number: 1
# Last digit: 1, Reversed number: 1, Remaining number: 0
# Reversed number is 1, which is not the same as the original 10. So, 10 is not a palindrome

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Roman to Integer

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999].

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Step 1: Create a mapping of Roman numerals to their integer values
        roman_to_int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Step 2: Initialize the total sum to 0
        total = 0

        # Step 3: Iterate through the string and calculate the integer value
        i = 0
        while i < len(s):
            # If the current character is the last one or its value is greater than or equal to the next one
            if i == len(s) - 1 or roman_to_int[s[i]] >= roman_to_int[s[i + 1]]:
                total += roman_to_int[s[i]]
            else:
                total -= roman_to_int[s[i]]
            i += 1

        return total

# Example usage
sol = Solution()
print(sol.romanToInt("III"))    # Output: 3
print(sol.romanToInt("LVIII"))  # Output: 58
print(sol.romanToInt("MCMXCIV")) # Output: 1994

# Example 1: s = "III"
# Iterate through: I (1) + I (1) + I (1)
# Total: 1 + 1 + 1 = 3

# Example 2: s = "LVIII"
# Iterate through: L (50) + V (5) + I (1) + I (1) + I (1)
# Total: 50 + 5 + 1 + 1 + 1 = 58

# Example 3: s = "MCMXCIV"
# Iterate through: M (1000) + CM (900) + XC (90) + IV (4)
# Total: 1000 + 900 + 90 + 4 = 1994

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Longest Common Prefix
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Step 1: Handle edge cases
        if not strs:
            return ""
        
        # Step 2: Initialize the prefix as the first string
        prefix = strs[0]
        
        # Step 3: Iterate through the strings
        for string in strs[1:]:
            # While the current prefix is not found at the start of the string, trim the prefix
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        
        return prefix

# Example usage
sol = Solution()
print(sol.longestCommonPrefix(["flower","flow","flight"]))  
print(sol.longestCommonPrefix(["dog","racecar","car"]))    

# Example 1:
# The list ["flower","flow","flight"] is passed to longestCommonPrefix
# The function initializes prefix to "flower" and then iteratively shortens it until it finds "fl" as the common prefix for all strings

# Example 2:
# The list ["dog","racecar","car"] is passed to longestCommonPrefix
# The function initializes prefix to "dog" and then shortens it to an empty string since there is no common prefix among the strings

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Valid Parentheses

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Stack to keep track of opening brackets
        stack = []
        
        # Dictionary to match opening and closing brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if it is not empty, otherwise assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the mapped bracket of the current char doesn't match the top element of the stack
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push the current opening bracket onto the stack
                stack.append(char)
        
        # If the stack is empty, all the brackets are properly closed
        return not stack
 
# Example Usage:
s = "()[]{}"
solution = Solution()
print(solution.isValid(s))  # Output: True

s = "(]"
print(solution.isValid(s))  # Output: False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Remove Duplicates from Sorted Array

# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 

# Constraints:

# 1 <= nums.length <= 3 * 104
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        # Initialize the counter for unique elements
        k = 1

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If the current element is not equal to the previous element
            if nums[i] != nums[i - 1]:
                # Assign the current element to the k-th position
                nums[k] = nums[i]
                # Increment the unique elements counter
                k += 1

        return k

nums = [0,0,1,1,1,2,2,3,3,4]
solution = Solution()
k = solution.removeDuplicates(nums)
print("Number of unique elements:", k)
print("Modified array:", nums[:k])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Remove Element

# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

# Example 1:

# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 
# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0  # Initialize the counter for elements not equal to val

        # Iterate through the array
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k

# Example usage:
solution = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = solution.removeElement(nums, val)
print("Number of elements not equal to val:", k)
print("Modified array:", nums[:k])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Merge Two Sorted Lists

# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:

# 1R -> 2R -> 4R
# 1P -> 3P -> 4P
# ------------
# 1P -> 1R -> 2R -> 3P -> 4R -> 4P

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class Solution(object):
#     def mergeTwoLists(self, list1, list2):
#         """
#         :type list1: Optional[ListNode]
#         :type list2: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         # Create a dummy node to start the merged list
#         dummy = ListNode()
#         current = dummy
        
#         # Traverse both lists
#         while list1 and list2:
#             if list1.val < list2.val:
#                 current.next = list1
#                 list1 = list1.next
#             else:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
        
#         # Append the remaining nodes
#         if list1:
#             current.next = list1
#         else:
#             current.next = list2
        
#         # Return the merged list, which starts from the next node of the dummy
#         return dummy.next

# # Function to print the list (for testing purposes)
# def print_list(node):
#     while node:
#         print str(node.val) + " ->",
#         node = node.next
#     print "None"

# # Create lists: list1 = [1,2,4], list2 = [1,3,4]
# list1 = ListNode(1, ListNode(2, ListNode(4)))
# list2 = ListNode(1, ListNode(3, ListNode(4)))

# # Additional test cases
# def create_linked_list(lst):
#     if not lst:
#         return None
#     head = ListNode(lst[0])
#     current = head
#     for val in lst[1:]:
#         current.next = ListNode(val)
#         current = current.next
#     return head

# def test_merge(list1_vals, list2_vals):
#     list1 = create_linked_list(list1_vals)
#     list2 = create_linked_list(list2_vals)
#     solution = Solution()
#     merged_list = solution.mergeTwoLists(list1, list2)
#     print_list(merged_list)

# # Test case 1: list1 = [1,2,4], list2 = [1,3,4]
# print("Test case 1:")
# test_merge([1, 2, 4], [1, 3, 4])

# # Test case 2: list1 = [], list2 = []
# print("Test case 2:")
# test_merge([], [])

# # Test case 3: list1 = [], list2 = [0]
# print("Test case 3:")
# test_merge([], [0])

# # Test case 4: list1 = [2, 5, 7], list2 = [1, 3, 4, 6]
# print("Test case 4:")
# test_merge([2, 5, 7], [1, 3, 4, 6])

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Find the Index of the First Occurrence in a String

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
    sol = Solution()
print(sol.strStr("sadbutsad", "sad"))  # Output: 0
print(sol.strStr("leetcode", "leeto"))  # Output: -1


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Search Insert Position

# Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:

# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:

# Input: nums = [1,3,5,6], target = 7
# Output: 4
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums contains distinct values sorted in ascending order.
# -104 <= target <= 104

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Length of Last Word

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

 

# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.
 

# Constraints:

# 1 <= s.length <= 104
# s consists of only English letters and spaces ' '.
# There will be at least one word in s.

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split()
        return len(words[-1])

# Example 1
s = "Hello World"
solution = Solution()
print(solution.lengthOfLastWord(s))  # Output: 5

# Example 2
s = "   fly me   to   the moon  "
print(solution.lengthOfLastWord(s))  # Output: 4

# Example 3
s = "luffy is still joyboy"
print(solution.lengthOfLastWord(s))  # Output: 6


# Plus One

# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.

 

# Example 1:

# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
# Example 2:

# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
# Example 3:

# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
 

# Constraints:

# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        # Start from the end of the array
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0
            digits[i] = 0
        
        # If all digits are 9, we need an extra digit at the beginning
        return [1] + [0] * n

# Example usage:
solution = Solution()
print(solution.plusOne([1, 2, 3]))  # Output: [1, 2, 4]
print(solution.plusOne([4, 3, 2, 1]))  # Output: [4, 3, 2, 2]
print(solution.plusOne([9]))  # Output: [1, 0]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Add Binary

# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # Initialize the result as an empty string and carry as 0
        result = ""
        carry = 0
        
        # Make both strings of equal length by padding with zeros
        max_length = max(len(a), len(b))
        a = a.zfill(max_length)
        b = b.zfill(max_length)
        
        # Iterate over the strings from the end to the beginning
        for i in range(max_length - 1, -1, -1):
            # Convert the binary characters to integers and add them along with the carry
            total_sum = int(a[i]) + int(b[i]) + carry
            carry = total_sum // 2  # Update the carry
            result = str(total_sum % 2) + result  # Append the current bit to the result
        
        # If there is any carry left, append it to the result
        if carry != 0:
            result = "1" + result
        
        return result

# Example usage:
solution = Solution()
print(solution.addBinary("11", "1"))  # Output: "100"
print(solution.addBinary("1010", "1011"))  # Output: "10101"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.
# Example 2:

# Input: x = 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

# Constraints:

# 0 <= x <= 231 - 1

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x

        left, right = 2, x // 2

        while left <= right:
            mid = (left + right) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

# Example usage:
sol = Solution()
print(sol.mySqrt(4))  # Output: 2
print(sol.mySqrt(8))  # Output: 2

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: n = 3
# Output: 3

# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# Constraints:

# 1 <= n <= 45

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize base cases
        first = 1
        second = 2
        
        # Calculate the number of ways for each step from 3 to n
        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        
        return second

solution = Solution()
print(solution.climbStairs(2))  # Output: 2
print(solution.climbStairs(3))  # Output: 3

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Example 1:

# Input: head = [1,1,2]
# Output: [1,2]
# Example 2:


# Input: head = [1,1,2,3,3]
# Output: [1,2,3]
 
# Constraints:

# The number of nodes in the list is in the range [0, 300].
# -100 <= Node.val <= 100
# The list is guaranteed to be sorted in ascending order.


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Start with the head of the list
        current = head
        
        # Iterate through the linked list
        while current and current.next:
            # If the current value is the same as the next value
            if current.val == current.next.val:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the modified list
        return head

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Merge Sorted Array

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109
 

# Follow up: Can you come up with an algorithm that runs in O(m + n) time?

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None
        """
        # Start from the end of both arrays
        p1 = m - 1  # Pointer for nums1
        p2 = n - 1  # Pointer for nums2
        p = m + n - 1  # Pointer for the end of the merged array
        
        # While there are still elements to compare in nums1 and nums2
        while p1 >= 0 and p2 >= 0:
            # Compare and place the larger element at the end of nums1
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are still elements left in nums2, copy them
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Binary Tree Inorder Traversal

# Given the root of a binary tree, return the inorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,3,2]

# Example 2:
# Input: root = []
# Output: []

# Example 3:
# Input: root = [1]
# Output: [1]
 
# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Helper function to perform inorder traversal
        def inorder(node):
            if node is None:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)
        
        # Start the inorder traversal from the root
        return inorder(root)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Same Tree

# Given the roots of two binary trees p and q, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example 1:
# Input: p = [1,2,3], q = [1,2,3]
# Output: true

# Example 2:
# Input: p = [1,2], q = [1,null,2]
# Output: false

# Example 3:
# Input: p = [1,2,1], q = [1,1,2]
# Output: false
 

# Constraints:

# The number of nodes in both trees is in the range [0, 100].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Base case: If both nodes are None, the trees are the same
        if not p and not q:
            return True
        
        # If one node is None and the other is not, the trees are not the same
        if not p or not q:
            return False
        
        # If the values of the current nodes are different, the trees are not the same
        if p.val != q.val:
            return False
        
        # Recursively check the left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Symmetric Tree

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Example 1:
# Input: root = [1,2,2,3,4,4,3]
# Output: true

# Example 2:
# Input: root = [1,2,2,null,3,null,3]
# Output: false
 
# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2:
                return False
            return (t1.val == t2.val) and \
                   isMirror(t1.left, t2.right) and \
                   isMirror(t1.right, t2.left)
        
        return isMirror(root, root)
  
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Maximum Depth of Binary Tree

# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2
 
# Constraints:

# The number of nodes in the tree is in the range [0, 104].
# -100 <= Node.val <= 100

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
    
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Convert Sorted Array to Binary Search Tree

# Given an integer array nums where the elements are sorted in ascending order, convert it to a 
# height-balanced
#  binary search tree.

# Example 1:
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:

# Example 2:
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

# Constraints:

# 1 <= nums.length <= 104
# -104 <= nums[i] <= 104
# nums is sorted in a strictly increasing order.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        
        def convertListToBST(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            
            node.left = convertListToBST(left, mid - 1)
            node.right = convertListToBST(mid + 1, right)
            
            return node
        
        return convertListToBST(0, len(nums) - 1)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Balanced Binary Tree

# Given a binary tree, determine if it is height-balanced.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: true

# Example 2:
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false

# Example 3:
# Input: root = []
# Output: true
 
# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -104 <= Node.val <= 104

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # Helper function to compute the height and check balance
        def checkHeight(node):
            if node is None:
                return 0
            
            # Recursively get the height of left and right subtrees
            left_height = checkHeight(node.left)
            right_height = checkHeight(node.right)
            
            # If left or right is unbalanced, propagate -1 up
            if left_height == -1 or right_height == -1:
                return -1
            
            # Check the height difference
            if abs(left_height - right_height) > 1:
                return -1
            else:
                return max(left_height, right_height) + 1

        # Start from the root and check the whole tree
        return checkHeight(root) != -1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.

# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

# Note: A leaf is a node with no children.

# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 2

# Example 2:
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5

# Constraints:

# The number of nodes in the tree is in the range [0, 105].
# -1000 <= Node.val <= 1000

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # If the current node is a leaf node
        if not root.left and not root.right:
            return 1
        
        # If the left subtree is missing, only consider the right subtree
        if not root.left:
            return self.minDepth(root.right) + 1
        
        # If the right subtree is missing, only consider the left subtree
        if not root.right:
            return self.minDepth(root.left) + 1
        
        # If both subtrees are present, consider the minimum of the two
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Path Sum

# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

# A leaf is a node with no children.

 

# Example 1:


# Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
# Output: true
# Explanation: The root-to-leaf path with the target sum is shown.

# Example 2:
# Input: root = [1,2,3], targetSum = 5
# Output: false
# Explanation: There two root-to-leaf paths in the tree:
# (1 --> 2): The sum is 3.
# (1 --> 3): The sum is 4.
# There is no root-to-leaf path with sum = 5.

# Example 3:
# Input: root = [], targetSum = 0
# Output: false
# Explanation: Since the tree is empty, there are no root-to-leaf paths.
 
# Constraints:

# The number of nodes in the tree is in the range [0, 5000].
# -1000 <= Node.val <= 1000
# -1000 <= targetSum <= 1000

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        # If we're at a leaf node, check if the current path sum equals targetSum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check the left and right subtrees
        return self.hasPathSum(root.left, targetSum - root.val) or \
               self.hasPathSum(root.right, targetSum - root.val)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

# Example 2:
# Input: numRows = 1
# Output: [[1]]

# Constraints:

# 1 <= numRows <= 30

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # Initialize the result list
        result = []
        
        for i in range(numRows):
            # Start each row with [1]
            row = [1] * (i + 1)
            
            # Fill in the interior values of the row
            for j in range(1, i):
                row[j] = result[i-1][j-1] + result[i-1][j]
            
            # Append the current row to the result list
            result.append(row)
        
        return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
# Pascal's Triangle II

# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]

# Example 2:
# Input: rowIndex = 0
# Output: [1]

# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
 
# Constraints:

# 0 <= rowIndex <= 33
 
# Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # Initialize the first row of Pascal's triangle
        row = [1] * (rowIndex + 1)
        
        # Update the row in place for each level of Pascal's Triangle
        for i in range(1, rowIndex):
            # Iterate backwards to ensure we use the previous row's values
            for j in range(i, 0, -1):
                row[j] += row[j - 1]
        
        return row

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Best Time to Buy and Sell Stock

# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Initialize min_price to a very high value and max_profit to 0
        min_price = float('inf')
        max_profit = 0
        
        # Loop through all prices
        for price in prices:
            # Update min_price if the current price is lower
            if price < min_price:
                min_price = price
            
            # Calculate potential profit
            profit = price - min_price
            
            # Update max_profit if this profit is higher
            if profit > max_profit:
                max_profit = profit
        
        return max_profit

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Valid Palindrome

# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.

# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.
 
# Constraints:

# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Normalize the string: convert to lowercase and filter out non-alphanumeric characters
        cleaned_string = ''.join(char.lower() for char in s if char.isalnum())
        
        # Check if the cleaned string is equal to its reverse
        return cleaned_string == cleaned_string[::-1]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Single Number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

# Constraints:

# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize a variable to store the result
        result = 0
        
        # XOR all numbers together
        for num in nums:
            result ^= num
        
        # The result will be the single number
        return result


# Linked List Cycle

# Given head, the head of a linked list, determine if the linked list has a cycle in it.

# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

# Example 2:
# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

# Example 3:
# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.
 
# Constraints:

# The number of the nodes in the list is in the range [0, 104].
# -105 <= Node.val <= 105
# pos is -1 or a valid index in the linked-list.
 
# Follow up: Can you solve it using O(1) (i.e. constant) memory?

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        
        # Initialize two pointers
        slow = head
        fast = head
        
        # Traverse the list
        while fast and fast.next:
            slow = slow.next            # Moves one step
            fast = fast.next.next       # Moves two steps
            
            # If the two pointers meet, there is a cycle
            if slow == fast:
                return True
        
        # If we exit the loop, there is no cycle
        return False

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Binary Tree Preorder Traversal

# Given the root of a binary tree, return the preorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]
# Output: [1,2,3]

# Explanation:

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
# Output: [1,2,4,5,6,7,3,8,9]

# Explanation:

# Example 3:
# Input: root = []

# Output: []

# Example 4:
# Input: root = [1]

# Output: [1] 

# Constraints:

# The number of nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100

# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # Edge case: if the root is None, return an empty list
        if not root:
            return []
        
        # Initialize a stack with the root node
        stack = [root]
        result = []
        
        # While there are nodes in the stack
        while stack:
            # Pop a node from the stack
            node = stack.pop()
            
            # Visit the node (add its value to the result list)
            result.append(node.val)
            
            # Push right child first (so that left child is processed first)
            if node.right:
                stack.append(node.right)
            
            # Push left child second
            if node.left:
                stack.append(node.left)
        
        return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

# Binary Tree Postorder Traversal

# Given the root of a binary tree, return the postorder traversal of its nodes' values.

# Example 1:
# Input: root = [1,null,2,3]

# Output: [3,2,1]

# Explanation:

# Example 2:
# Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

# Output: [4,6,7,5,2,9,8,3,1]

# Explanation:

# Example 3:
# Input: root = []

# Output: []

# Example 4:
# Input: root = [1]

# Output: [1]

# Constraints:

# The number of the nodes in the tree is in the range [0, 100].
# -100 <= Node.val <= 100
 
# Follow up: Recursive solution is trivial, could you do it iteratively?

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack1 = [root]
        stack2 = []
        result = []
        
        # Process all nodes
        while stack1:
            node = stack1.pop()
            stack2.append(node)
            
            # Push left and right children to stack1
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        # Stack2 will have nodes in postorder order
        while stack2:
            node = stack2.pop()
            result.append(node.val)
        
        return result

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
