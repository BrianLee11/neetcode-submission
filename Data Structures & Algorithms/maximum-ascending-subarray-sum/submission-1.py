"""
# 1800. Maximum Ascending Subarray Sum
- Start date/time: 2026-07-31 08:05:
- End date/time: 2026-07-31 08:28:51
- difficulty: easy

## NeetCode
- topic: arrays and hashing
- url: https://neetcode.io/problems/maximum-ascending-subarray-sum/question

## LeetCode
- url: https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
"""
from typing import List

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        int_max_sum = nums[0]
        int_current_sum = nums[0]
        for index in range(1, len(nums), 1):
            # strictly increasing
            if nums[index] > nums[index - 1]:
                int_current_sum += nums[index]
            else:
                int_current_sum = nums[index]

            if int_max_sum < int_current_sum:
                int_max_sum = int_current_sum

        return int_max_sum
