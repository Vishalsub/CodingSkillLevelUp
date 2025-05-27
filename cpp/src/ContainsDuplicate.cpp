#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

class Solution {
public:

    bool bruteForce(vector<int>& nums){
        std::sort(nums.begin(), nums.end());
        for(int i = 0; i < nums.size(); i++){
            for(int j = i+1; j < nums.size(); j++){
                if(nums[i] == nums[j]){
                    return true;
                }
            }
        }
        return false;
    }
    bool optimalSolution(vector<int>& nums) {
        unordered_set<int> seen;
        for (const int num : nums) {
            if (seen.find(num) != seen.end()) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};

int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 1};  // Example input
    vector<int> num_ = {1, 2, 3, 4, 35};  // Example input
    bool result = sol.bruteForce(nums);
    bool result_ = sol.optimalSolution(num_);
    cout << "Contains duplicate? " << (result ? "Yes" : "No") << endl;
    cout << "Contains duplicate? " << (result_ ? "Yes" : "No") << endl;
    return 0;
}
