/* LeetCode Q.242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description/
*/

#include <iostream>
#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> charIntMapS;
        unordered_map<char, int> charIntMapT;

        for (char character : s){
            charIntMapS[character]++;
        }

        for (char character : t){
            charIntMapT[character]++;
        }

        for (const auto&[key, value] : charIntMapS){
            if (charIntMapT.find(key) == charIntMapT.end()){
                return false;        
            }
            else {
                if (charIntMapS[key] != charIntMapT[key]){
                    return false;
                }
            }
        }

        for (const auto&[key, value] : charIntMapT){
            if (charIntMapS.find(key) == charIntMapS.end()){
                return false;        
            }
            else {
                if (charIntMapT[key] != charIntMapS[key]){
                    return false;
                }
            }
        }

        // otherwise, print true
        return true;
    }
};
