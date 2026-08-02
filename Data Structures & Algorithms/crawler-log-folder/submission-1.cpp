#include <iostream>
#include <vector>
#include <string>
#include <queue>
using namespace std;

class Solution {
public:
    int minOperations(vector<string>& logs) {        
        queue<string> folders;
        for (string log : logs){
            if (log == "./"){
                continue;
            }
            else if (log == "../"){
                if (! folders.empty()){
                    folders.pop();
                }
            }
            else{
                folders.push(log);
            }
        }

        queue<string> foldersCopy = folders;
        int countFolders = 0;
        while (! foldersCopy.empty()){
            foldersCopy.pop();
            countFolders += 1;    
        }

            return countFolders;
    }
};