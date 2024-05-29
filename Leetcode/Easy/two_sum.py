"""
Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Can you come up with an algorithm that is less than O(n2) time complexity?

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
"""
from typing import List


class Solution:
    def twoSum_not_efficient(self, nums: List[int], target: int) -> List[int]:
        return [(i, j) for i, x in enumerate(nums) for j, y in enumerate(nums) if i != j and x + y == target]

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num_to_index = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen_num_to_index:
                return [seen_num_to_index[complement], i]
            # Otherwise, add the current number to the dictionary
            seen_num_to_index[num] = i

        return []


print(Solution().twoSum_not_efficient([2,7,11,15], 9))
print(Solution().twoSum([2,7,11,15], 9))
print(Solution().twoSum([3,2, 3, 4], 6))
print(Solution().twoSum([3,3], 6))
print(Solution().twoSum([3,5,1,2], 6))
print(Solution().twoSum([3,4], 6))
print(Solution().twoSum([3,2,4], 1))
print(Solution().twoSum([], 6))