#include <iostream>
#include <vector>
#include <set>
using namespace std;

class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> setNumbers;

        for (int number :nums){
            if (setNumbers.find(number) != setNumbers.end()){
                return true;
            }
            else {
                setNumbers.insert(number);
            }
        }
        return false;
    }
};