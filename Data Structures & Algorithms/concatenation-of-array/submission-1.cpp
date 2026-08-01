#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> concatenatedNums = nums;

        for (int integer : nums) {
            concatenatedNums.push_back(integer);
        }
        return concatenatedNums;
    }
};
