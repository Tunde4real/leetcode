'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # runs in 0 - 3 ms
        seen = {}
        for index, i in enumerate(nums):
            j = target - i
            try:
                seen[j]
                return [index, seen[j]]
            except: seen[i] = index
        
        # runs in 1700 - 1811 ms
        for index, i in enumerate(nums):
            ind = index + 1
            num = nums[ind:]
            for j in num:
                if i + j == target:
                    return [index, ind]
                else:
                    ind += 1