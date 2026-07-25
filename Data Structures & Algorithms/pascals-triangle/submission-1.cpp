#include <iostream>
#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (numRows == 1) {return vector<vector<int>> {{1}};}
        else if (numRows == 2) {return vector<vector<int>> {{1},{1,1}};}
        else if (numRows == 3) {return vector<vector<int>> {{1}, {1,1}, {1,2,1}};}
        else
        {
            map<int, vector<int>> map_triangle = {
                {1, {1}},
                {2, {1,1}},
                {3, {1,2,1}}
            };

            vector<vector<int>> combined_triangles = {
                {1},
                {1,1},
                {1,2,1}
            };

            for (int index = 4; index < numRows + 1; ++index)
            {
                vector<int> target_triangle = map_triangle[index -1];
                vector<int> receive_array = {1};
                for (size_t triangle_index = 0; triangle_index < (target_triangle.size() - 1); ++triangle_index)
                {
                    receive_array.push_back(target_triangle[triangle_index] + target_triangle[triangle_index + 1]);
                }
                receive_array.push_back(1);

                map_triangle[index] = receive_array;
                combined_triangles.push_back(receive_array);
            }

            return combined_triangles;        
        }
    }
};