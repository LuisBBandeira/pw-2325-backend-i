"""
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

"""
import unittest

def solution(nums:list[int], target:int)->list[int]: 
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    raise Exception("Was not possible to find indexes")


class TestTwoSum(unittest.TestCase):

    def test_case_1(self):
        nums = [2,7,11,15]
        target = 9
        result = solution(nums=nums,target=target)
        solution_target = [0,1]
        self.assertEqual(result,solution_target)

    def test_case_2(self):
        nums = [3,2,4]
        target = 6
        result = solution(nums=nums,target=target)
        solution_target = [1,2]
        self.assertEqual(result,solution_target)

    def test_case_3(self):
        nums = [3,3]
        target = 6
        result = solution(nums=nums,target=target)
        solution_target = [0,1]
        self.assertEqual(result,solution_target)


if __name__ == "__main__":
    unittest.main()
