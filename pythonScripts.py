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
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  
print(solution.twoSum([3, 2, 4], 6))      
print(solution.twoSum([3, 3], 6))          