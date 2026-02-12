class Solution {
public:
    bool is_substring_balanced(const std::unordered_map<char, int>& substring_map) {
        if (substring_map.empty()) return true;
        int first_value = substring_map.begin()->second;
        return std::all_of(
            substring_map.begin(), substring_map.end(),
            [&](const auto& p) {
                return p.second == first_value;
            }
        );
    }

    int longestBalanced(string s) {
        int res = 0;
        for (int i=0; i<s.size(); i++) {
            std::unordered_map<char, int> substring_map;
            for (int j=i; j<s.size(); j++) {
                substring_map[s[j]]++;
                if (is_substring_balanced(substring_map)) 
                    res = max(res, j-i+1);
            }
        }
        return res;
    }
};
