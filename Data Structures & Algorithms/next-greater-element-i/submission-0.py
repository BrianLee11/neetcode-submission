from typing import List

class Solution:
    @staticmethod
    def findNextGreaterElement(index: int, array: List[int]) -> int:
        target_number = array[index]
        target_array = array[index + 1:]
        for number in target_array:
            if target_number < number:
                return number
        return -1

    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list_int_output_array = []
        for number in nums1:
            int_index_num2 = nums2.index(number)
            int_next_greateer_element = self.findNextGreaterElement(int_index_num2, nums2)
            list_int_output_array.append(int_next_greateer_element)
        return list_int_output_array