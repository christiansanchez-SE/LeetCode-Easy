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
