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
        # Step 1: Check if the number is negative
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