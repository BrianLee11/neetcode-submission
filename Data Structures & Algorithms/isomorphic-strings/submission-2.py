from collections import defaultdict
from collections import Counter

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary_s = defaultdict(list)
        dictionary_t = defaultdict(list)

        for index, character in enumerate(s):
            dictionary_s[character].append(index)
    
        for index, character in enumerate(t):
            dictionary_t[character].append(index)
        
        set_tuple_s = set(tuple(value) for value in dictionary_s.values())
        set_tuple_t = set(tuple(value) for value in dictionary_t.values())        

        return Counter(set_tuple_s) == Counter(set_tuple_t)