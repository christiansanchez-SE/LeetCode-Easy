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

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    // Step 1: Check if the number is negative
    if (x < 0) {
        return false;  
    }

    // Step 2: Store the original number
    let original = x;

    // Step 3: Reverse the digits of the number
    let reversedNum = 0;
    while (x > 0) {
        let lastDigit = x % 10;          
        reversedNum = reversedNum * 10 + lastDigit;  
        x = Math.floor(x / 10);  
    }

    // Step 4: Compare the original and reversed numbers
    return original === reversedNum;  
};

// Example usage
console.log(isPalindrome(121));  
console.log(isPalindrome(-121)); 
console.log(isPalindrome(10));   

// Example 1: x = 121
// Initial number: 121
// Reverse process:
// Last digit: 1, Reversed number: 1, Remaining number: 12
// Last digit: 2, Reversed number: 12, Remaining number: 1
// Last digit: 1, Reversed number: 121, Remaining number: 0
// Reversed number is 121, which is the same as the original. So, 121 is a palindrome

// Example 2: x = -121
// The number is negative. Immediately return false

// Example 3: x = 10
// Initial number: 10
// Reverse process:
// Last digit: 0, Reversed number: 0, Remaining number: 1
// Last digit: 1, Reversed number: 1, Remaining number: 0
// Reversed number is 1, which is not the same as the original 10. So, 10 is not a palindrome

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    // Step 1: Create a mapping of Roman numerals to their integer values
    const romanToInt = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    };

    // Step 2: Initialize the total sum to 0
    let total = 0;

    // Step 3: Iterate through the string and calculate the integer value
    for (let i = 0; i < s.length; i++) {
        // If the current character is the last one or its value is greater than or equal to the next one
        if (i === s.length - 1 || romanToInt[s[i]] >= romanToInt[s[i + 1]]) {
            total += romanToInt[s[i]];
        } else {
            total -= romanToInt[s[i]];
        }
    }

    return total;
};

// Example usage
console.log(romanToInt("III"));    // Output: 3
console.log(romanToInt("LVIII"));  // Output: 58
console.log(romanToInt("MCMXCIV")); // Output: 1994

// Example 1: s = "III"
// Iterate through: I (1) + I (1) + I (1)
// Total: 1 + 1 + 1 = 3

// Example 2: s = "LVIII"
// Iterate through: L (50) + V (5) + I (1) + I (1) + I (1)
// Total: 50 + 5 + 1 + 1 + 1 = 58

// Example 3: s = "MCMXCIV"
// Iterate through: M (1000) + CM (900) + XC (90) + IV (4)
// Total: 1000 + 900 + 90 + 4 = 1994

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

// Longest Common Prefix

/**
 * @param {string[]} strs
 * @return {string}
 */
var longestCommonPrefix = function(strs) {
    // Step 1: Handle edge cases
    if (strs.length === 0) {
        return "";
    }

    // Step 2: Initialize the prefix as the first string
    let prefix = strs[0];

    // Step 3: Iterate through the strings
    for (let i = 1; i < strs.length; i++) {
        // While the current prefix is not found at the start of the string, trim the prefix
        while (strs[i].indexOf(prefix) !== 0) {
            prefix = prefix.substring(0, prefix.length - 1);
            if (prefix === "") {
                return "";
            }
        }
    }

    return prefix;
};

// Example usage
console.log(longestCommonPrefix(["flower", "flow", "flight"]));  // Output: "fl"
console.log(longestCommonPrefix(["dog", "racecar", "car"]));    // Output: ""

// Example 1: ["flower", "flow", "flight"]
// prefix is initialized to "flower"
// "flower" and "flow" share the prefix "flow"
// "flow" and "flight" share the prefix "fl"
// The function returns "fl"

// Example 2: ["dog", "racecar", "car"]
// prefix is initialized to "dog"
// "dog" and "racecar" share no common prefix, so prefix is reduced to an empty string
// The function returns an empty string

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

var isValid = function(s) {
    // Stack to keep track of opening brackets
    let stack = [];
    
    // Dictionary to match opening and closing brackets
    let bracketMap = {
        ')': '(',
        '}': '{',
        ']': '['
    };
    
    for (let char of s) {
        if (char in bracketMap) {
            // Pop the top element from the stack if it is not empty, otherwise assign a dummy value
            let topElement = stack.length ? stack.pop() : '#';
            
            // If the mapped bracket of the current char doesn't match the top element of the stack
            if (bracketMap[char] !== topElement) {
                return false;
            }
        } else {
            // Push the current opening bracket onto the stack
            stack.push(char);
        }
    }
    
    // If the stack is empty, all the brackets are properly closed
    return stack.length === 0;
};

// Example Usage:
console.log(isValid("()"));      // Output: true
console.log(isValid("()[]{}"));  // Output: true
console.log(isValid("(]"));      // Output: false

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    if (nums.length === 0) return 0;

    let k = 1; // Start with the first element being unique

    for (let i = 1; i < nums.length; i++) {
        if (nums[i] !== nums[i - 1]) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;
};

// Example usage:
// const nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4];
// const k = removeDuplicates(nums);

// console.log("Number of unique elements:", k);
// console.log("Modified array:", nums.slice(0, k));

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    let k = 0;  // Initialize the counter for elements not equal to val

    // Iterate through the array
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== val) {
            nums[k] = nums[i];
            k++;
        }
    }

    return k;
};

// Example usage:
const nums = [0, 1, 2, 2, 3, 0, 4, 2];
const val = 2;
const k = removeElement(nums, val);

console.log("Number of elements not equal to val:", k);
console.log("Modified array:", nums.slice(0, k));

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
    // Create a dummy node to start the merged list
    let dummy = new ListNode();
    let current = dummy;
    
    // Traverse both lists
    while (list1 !== null && list2 !== null) {
        if (list1.val < list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }
    
    // Append the remaining nodes
    if (list1 !== null) {
        current.next = list1;
    } else {
        current.next = list2;
    }
    
    // Return the merged list, which starts from the next node of the dummy
    return dummy.next;
};

// Function to print the list (for testing purposes)
function printList(node) {
    let result = '';
    while (node !== null) {
        result += node.val + ' -> ';
        node = node.next;
    }
    result += 'None';
    console.log(result);
}

// Create linked lists for testing
function createLinkedList(arr) {
    if (arr.length === 0) {
        return null;
    }
    let head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}

// Test case 1: list1 = [1, 2, 4], list2 = [1, 3, 4]
console.log("Test case 1:");
printList(mergeTwoLists(createLinkedList([1, 2, 4]), createLinkedList([1, 3, 4])));

// Test case 2: list1 = [], list2 = []
console.log("Test case 2:");
printList(mergeTwoLists(createLinkedList([]), createLinkedList([])));

// Test case 3: list1 = [], list2 = [0]
console.log("Test case 3:");
printList(mergeTwoLists(createLinkedList([]), createLinkedList([0])));

// Test case 4: list1 = [2, 5, 7], list2 = [1, 3, 4, 6]
console.log("Test case 4:");
printList(mergeTwoLists(createLinkedList([2, 5, 7]), createLinkedList([1, 3, 4, 6])));

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */
var strStr = function(haystack, needle) {
    return haystack.indexOf(needle);
};

// Example usage:
console.log(strStr("sadbutsad", "sad"));  // Output: 0
console.log(strStr("leetcode", "leeto")); // Output: -1

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var searchInsert = function(nums, target) {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);

        if (nums[mid] === target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return left;
};

// Example usage:
console.log(searchInsert([1, 3, 5, 6], 5)); // Output: 2
console.log(searchInsert([1, 3, 5, 6], 2)); // Output: 1
console.log(searchInsert([1, 3, 5, 6], 7)); // Output: 4

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    // Trim any leading or trailing spaces
    s = s.trim();
    // Split the string into words based on spaces
    let words = s.split(' ');
    // Return the length of the last word
    return words[words.length - 1].length;
};

// Example 1
let s1 = "Hello World";
console.log(lengthOfLastWord(s1)); // Output: 5

// Example 2
let s2 = "   fly me   to   the moon  ";
console.log(lengthOfLastWord(s2)); // Output: 4

// Example 3
let s3 = "luffy is still joyboy";
console.log(lengthOfLastWord(s3)); // Output: 6

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    let n = digits.length;
    
    // Start from the end of the array
    for (let i = n - 1; i >= 0; i--) {
        if (digits[i] < 9) {
            digits[i] += 1;
            return digits;
        }
        // If the digit is 9, it becomes 0
        digits[i] = 0;
    }
    
    // If all digits are 9, we need an extra digit at the beginning
    digits.unshift(1);
    return digits;
};

// Example usage:
console.log(plusOne([1, 2, 3]));  // Output: [1, 2, 4]
console.log(plusOne([4, 3, 2, 1]));  // Output: [4, 3, 2, 2]
console.log(plusOne([9]));  // Output: [1, 0]

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {string} a
 * @param {string} b
 * @return {string}
 */
var addBinary = function(a, b) {
    let result = "";
    let carry = 0;
    
    // Make both strings of equal length by padding with zeros
    let maxLength = Math.max(a.length, b.length);
    a = a.padStart(maxLength, '0');
    b = b.padStart(maxLength, '0');
    
    // Iterate over the strings from the end to the beginning
    for (let i = maxLength - 1; i >= 0; i--) {
        // Convert the binary characters to integers and add them along with the carry
        let sum = parseInt(a[i]) + parseInt(b[i]) + carry;
        carry = Math.floor(sum / 2);  // Update the carry
        result = (sum % 2) + result;  // Append the current bit to the result
    }
    
    // If there is any carry left, append it to the result
    if (carry !== 0) {
        result = '1' + result;
    }
    
    return result;
};

// Example usage:
console.log(addBinary("11", "1"));  // Output: "100"
console.log(addBinary("1010", "1011"));  // Output: "10101"

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number} x
 * @return {number}
 */
var mySqrt = function(x) {
    if (x < 2) {
        return x;
    }

    let left = 2, right = Math.floor(x / 2);

    while (left <= right) {
        let mid = Math.floor((left + right) / 2);
        let num = mid * mid;

        if (num === x) {
            return mid;
        } else if (num < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return right;
};

// Example usage:
console.log(mySqrt(4));  // Output: 2
console.log(mySqrt(8));  // Output: 2

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n === 1) {
        return 1;
    }
    if (n === 2) {
        return 2;
    }

    // Initialize base cases
    let first = 1;
    let second = 2;

    // Calculate the number of ways for each step from 3 to n
    for (let i = 3; i <= n; i++) {
        let third = first + second;
        first = second;
        second = third;
    }

    return second;
};

console.log(climbStairs(2)); // Output: 2
console.log(climbStairs(3)); // Output: 3
console.log(climbStairs(5)); // Output: 8

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val);
 *     this.next = (next===undefined ? null : next);
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var deleteDuplicates = function(head) {
    // Start with the head of the list
    let current = head;
    
    // Iterate through the linked list
    while (current !== null && current.next !== null) {
        // If the current value is the same as the next value
        if (current.val === current.next.val) {
            // Skip the next node
            current.next = current.next.next;
        } else {
            // Move to the next node
            current = current.next;
        }
    }
    
    // Return the modified list
    return head;
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    // Start from the end of both arrays
    let p1 = m - 1;  // Pointer for nums1
    let p2 = n - 1;  // Pointer for nums2
    let p = m + n - 1;  // Pointer for the end of the merged array
    
    // While there are still elements to compare in nums1 and nums2
    while (p1 >= 0 && p2 >= 0) {
        // Compare and place the larger element at the end of nums1
        if (nums1[p1] > nums2[p2]) {
            nums1[p] = nums1[p1];
            p1--;
        } else {
            nums1[p] = nums2[p2];
            p2--;
        }
        p--;
    }
    
    // If there are still elements left in nums2, copy them
    while (p2 >= 0) {
        nums1[p] = nums2[p2];
        p2--;
        p--;
    }
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    // Helper function to perform inorder traversal
    const inorder = (node) => {
        if (node === null) {
            return [];
        }
        return [...inorder(node.left), node.val, ...inorder(node.right)];
    };
    
    // Start the inorder traversal from the root
    return inorder(root);
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
var isSameTree = function(p, q) {
    if (!p && !q) {
        return true;
    }
    if (!p || !q) {
        return false;
    }
    if (p.val !== q.val) {
        return false;
    }
    return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    // Helper function to check if two trees are mirror images
    const isMirror = (t1, t2) => {
        if (!t1 && !t2) {
            return true;
        }
        if (!t1 || !t2) {
            return false;
        }
        return (t1.val === t2.val) &&
               isMirror(t1.left, t2.right) &&
               isMirror(t1.right, t2.left);
    };

    // Start the mirror check from the root's left and right children
    return isMirror(root, root);
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val === undefined ? 0 : val);
 *     this.left = (left === undefined ? null : left);
 *     this.right = (right === undefined ? null : right);
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxDepth = function(root) {
    if (root === null) {
        return 0;
    } else {
        const leftDepth = maxDepth(root.left);
        const rightDepth = maxDepth(root.right);
        return Math.max(leftDepth, rightDepth) + 1;
    }
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val === undefined ? 0 : val);
 *     this.left = (left === undefined ? null : left);
 *     this.right = (right === undefined ? null : right);
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    if (!nums.length) return null;

    function convertListToBST(left, right) {
        if (left > right) return null;

        let mid = Math.floor((left + right) / 2);
        let node = new TreeNode(nums[mid]);

        node.left = convertListToBST(left, mid - 1);
        node.right = convertListToBST(mid + 1, right);

        return node;
    }

    return convertListToBST(0, nums.length - 1);
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isBalanced = function(root) {
    // Helper function to check height and balance
    function checkHeight(node) {
        if (node === null) return 0;

        // Recursively get the height of the left and right subtree
        let leftHeight = checkHeight(node.left);
        let rightHeight = checkHeight(node.right);

        // If the subtree is already unbalanced, return -1
        if (leftHeight === -1 || rightHeight === -1) return -1;

        // If the current node causes the tree to be unbalanced
        if (Math.abs(leftHeight - rightHeight) > 1) return -1;

        // Otherwise, return the height of the tree from the current node
        return Math.max(leftHeight, rightHeight) + 1;
    }

    // An initial check from the root if it returns -1, then it's unbalanced
    return checkHeight(root) !== -1;
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var minDepth = function(root) {
    if (root === null) {
        return 0;
    }

    // If the current node is a leaf node
    if (root.left === null && root.right === null) {
        return 1;
    }

    // If the left subtree is missing, only consider the right subtree
    if (root.left === null) {
        return minDepth(root.right) + 1;
    }

    // If the right subtree is missing, only consider the left subtree
    if (root.right === null) {
        return minDepth(root.left) + 1;
    }

    // If both subtrees are present, consider the minimum of the two
    return Math.min(minDepth(root.left), minDepth(root.right)) + 1;
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    if (root === null) {
        return false;
    }

    // If the current node is a leaf node, check if the targetSum equals the node's value
    if (root.left === null && root.right === null) {
        return targetSum === root.val;
    }

    // Recursively check the left and right subtrees with the updated targetSum
    return hasPathSum(root.left, targetSum - root.val) || hasPathSum(root.right, targetSum - root.val);
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    // Initialize the result array
    let result = [];
    
    for (let i = 0; i < numRows; i++) {
        // Start each row with [1]
        let row = Array(i + 1).fill(1);
        
        // Fill in the interior values of the row
        for (let j = 1; j < i; j++) {
            row[j] = result[i - 1][j - 1] + result[i - 1][j];
        }
        
        // Append the current row to the result array
        result.push(row);
    }
    
    return result;
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    // Initialize the first row of Pascal's triangle
    let row = new Array(rowIndex + 1).fill(1);
    
    // Update the row in place for each level of Pascal's Triangle
    for (let i = 1; i < rowIndex; i++) {
        // Iterate backwards to ensure we use the previous row's values
        for (let j = i; j > 0; j--) {
            row[j] += row[j - 1];
        }
    }
    
    return row;
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    // Initialize min_price to a very high value and max_profit to 0
    let min_price = Infinity;
    let max_profit = 0;
    
    // Loop through all prices
    for (let price of prices) {
        // Update min_price if the current price is lower
        if (price < min_price) {
            min_price = price;
        }
        
        // Calculate potential profit
        let profit = price - min_price;
        
        // Update max_profit if this profit is higher
        if (profit > max_profit) {
            max_profit = profit;
        }
    }
    
    return max_profit;
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // Normalize the string: convert to lowercase and remove non-alphanumeric characters
    let cleanedString = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    
    // Check if the cleaned string is equal to its reverse
    return cleanedString === cleanedString.split('').reverse().join('');
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    // Initialize a variable to store the result
    let result = 0;
    
    // XOR all numbers together
    for (let num of nums) {
        result ^= num;
    }
    
    // The result will be the single number
    return result;
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    if (!head || !head.next) {
        return false;
    }
    
    // Initialize two pointers, slow and fast
    let slow = head;
    let fast = head;
    
    // Traverse the list
    while (fast !== null && fast.next !== null) {
        slow = slow.next;          // Move slow by 1 step
        fast = fast.next.next;     // Move fast by 2 steps
        
        // If slow and fast pointers meet, there is a cycle
        if (slow === fast) {
            return true;
        }
    }
    
    // If the fast pointer reaches the end, there is no cycle
    return false;
};

//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal = function(root) {
    if (!root) {
        return [];
    }
    
    let stack1 = [root];
    let stack2 = [];
    let result = [];
    
    // Traverse the tree
    while (stack1.length > 0) {
        let node = stack1.pop();
        stack2.push(node);
        
        // Push left and right children to stack1
        if (node.left) {
            stack1.push(node.left);
        }
        if (node.right) {
            stack1.push(node.right);
        }
    }
    
    // Extract nodes from stack2 to result (postorder traversal)
    while (stack2.length > 0) {
        let node = stack2.pop();
        result.push(node.val);
    }
    
    return result;
};


//  - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - //
