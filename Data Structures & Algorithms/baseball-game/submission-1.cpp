#include <iostream>
#include <vector>
#include <string>
#include <deque>
using namespace std;

class Solution {
public:
    int calPoints(vector<string>& operations) {
        deque<int> queueInt;

        for (string op: operations){
            if (op == "+"){
                int firstLastNumber = queueInt.back();
                queueInt.pop_back();        

                int secondLastNumber = queueInt.back();
                int sumNumber = firstLastNumber + secondLastNumber;

                queueInt.push_back(firstLastNumber);
                queueInt.push_back(sumNumber);
            }

            else if (op == "D"){
                int firstLastNumber = queueInt.back();    
                int doubledNumber = firstLastNumber * 2;        
                queueInt.push_back(doubledNumber);
            }

            else if (op == "C"){
                queueInt.pop_back();
            }

            else{
                queueInt.push_back(stoi(op));
            }    
        }

        int sumInt = 0;
        while (! queueInt.empty()){
            int lastInt = queueInt.back();
            sumInt += lastInt;
            queueInt.pop_back();
        }

        return sumInt;
    }
};