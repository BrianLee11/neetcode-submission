# LeetCode
# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/

# NeetCode
# https://neetcode.io/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/question?list=allNC

# Start date/time: 2026-07-30 12:49
# End date/time: 2026-07-30 13:09:10

from typing import List
from enum import Enum

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        # trivail cases: when length is 0 or 1
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        # enum for faster implementation/process
        class Status(Enum):
            INCREASING = 1
            DECREASING = 2
            CONSTANT = 3

        # initialize
        first_number = nums[0]
        second_number = nums[1]
        previous_status = Status.CONSTANT
        current_count = 0
        max_count = 1

        # the first relationship
        if first_number < second_number:
            previous_status = Status.INCREASING
            current_count += 2
        elif first_number > second_number:
            previous_status = Status.DECREASING
            current_count += 2
        elif first_number == second_number:
            current_count += 1

        # iterate the rest of the relationship
        for index in range(1, len(nums) - 1, 1):
            current_status = Status.CONSTANT
            first_number = nums[index]
            second_number = nums[index + 1]

            # compute current status
            if first_number < second_number:
                current_status = Status.INCREASING

            elif first_number > second_number:
                current_status = Status.DECREASING

            elif first_number == second_number:
                current_count = 1

            # compare current status with previous status
            if current_status != Status.CONSTANT:
                if previous_status != current_status:
                    current_count = 2                # reset the count
                    previous_status = current_status # reset the relationship

                else:
                    current_count += 1 # increment count, if the same status

                # update the maximum value
                if current_count > max_count:
                    max_count = current_count

        return max_count
