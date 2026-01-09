#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

class Solution {
public:
    bool isValid(string s) {
        if (s.size() % 2 != 0) { return false; }

        std::vector<char> close_first;
        std::unordered_map<char, char> bracket_map = {
            {'(', ')'},
            {'{', '}'},
            {'[', ']'}
        };

        for (char pa : s) {
            if (bracket_map.count(pa)) {
                close_first.push_back(bracket_map[pa]);
            }
            else {
                if (close_first.empty() || close_first.back() != pa) {
                    return false;
                }
                close_first.pop_back();
            }
        }

        return close_first.empty();
    }
};
