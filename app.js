// Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

// You may assume that each input would have exactly one solution, and you may not use the same element twice.

// You can return the answer in any order.

 

// Example 1:

// Input: nums = [2,7,11,15], target = 9
// Output: [0,1]
// Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
// Example 2:

// Input: nums = [3,2,4], target = 6
// Output: [1,2]
// Example 3:

// Input: nums = [3,3], target = 6
// Output: [0,1]
 

// Constraints:

// 2 <= nums.length <= 104
// -109 <= nums[i] <= 109
// -109 <= target <= 109
// Only one valid answer exists.
 

// Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */

// nums: An array of integers
// target: An integer that represents the sum we want to achieve by adding two numbers from the nums array
var twoSum = function(nums, target) {

    // Create a dictionary to store the value and its index
    let numDict = {};

    // We use a for loop to iterate through each number in the nums array
    for (let index = 0; index < nums.length; index++) {
        // index is the current position in the array
        // num is the value of the number at the current position
        let num = nums[index];
        // For each number num, we calculate its complement by subtracting num from the target
        let complement = target - num;

        // Check if the complement exists in the dictionary
        // If it does, it means we have found the two numbers that add up to the target (num and complement)
        if (complement in numDict) {
            // Return the indices of the two numbers that add up to the target
            return [numDict[complement], index];
        }

        // Store the current number and its index in the dictionary
            // If the complement is not found in the dictionary, we add the current number num and its index to the dictionary
        numDict[num] = index;
    }
};

// Example usage:
console.log(twoSum([2, 7, 11, 15], 9));  // Output: [0, 1]
console.log(twoSum([3, 2, 4], 6));       // Output: [1, 2]
console.log(twoSum([3, 3], 6));          // Output: [0, 1]


//  How it works for example one
    // Iteration 1: index = 0, num = 2 : complement = 9 - 2 = 7 : 7 is not in numDict : Update numDict to {2: 0}
    // Iteration 2: index = 1, num = 7 : complement = 9 - 7 = 2 : 2 is in numDict with index 0
    // Return [0, 1]

// How it works for example two
    // Iteration 1: index = 0, num = 3 : complement = 6 - 3 = 3 : 3 is not in numDict : Update numDict to {3: 0}
    // Iteration 2: index = 1, num = 2 : complement = 6 - 2 = 4 : 4 is not in numDict : Update numDict to {3: 0, 2: 1}
    // Iteration 3: index = 2, num = 4 : complement = 6 - 4 = 2 : 2 is in numDict with index 1 
    // Return [1, 2]

// How it works for example three
    // Iteration 1: index = 0, num = 3 : complement = 6 - 3 = 3 : 3 is not in numDict : Update numDict to {3: 0}
    // Iteration 2: index = 1, num = 3 : complement = 6 - 3 = 3 : 3 is in numDict with index 0
    // Return [0, 1]