from collections import defaultdict

class Solution:
    def maxDifference(self, s: str) -> int:
        dictionary_char = defaultdict(int)

        for character in s:
            dictionary_char[character] += 1        

        list_odd_sorted = sorted((value for value in dictionary_char.values() if value % 2 == 1), reverse = True)
        list_even_sorted = sorted((value for value in dictionary_char.values() if value % 2 == 0), reverse = False)
        
        return list_odd_sorted[0] - list_even_sorted[0]