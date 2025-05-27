       /*
        Example 1:
        Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
        
        Example 2:
        Input: strs = ["x"]
        Output: [["x"]]

        Example 3:
        Input: strs = [""]
        Output: [[""]]
        
        Create a hashmap to store groups
        Loop through each word in the input list:
        Sort the word alphabetically -> (this becomes your anagram key)
        Insert the word into the map under that key
        Return all the grouped values from the hashmap
       */

#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<string>> GroupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> anagramMap;

        for (const string& word : strs) {
            string sortedWord = word;
            sort(sortedWord.begin(), sortedWord.end());
            anagramMap[sortedWord].push_back(word);
        }

        vector<vector<string>> result;
        for (const auto& pair : anagramMap) {
            result.push_back(pair.second);
        }

        return result;
    }
};


