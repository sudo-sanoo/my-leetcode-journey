class Solution {
public:
    bool isPalindrome(std::string s) {
        int start = 0;
        int end = s.size() - 1;
        while (start <= end) {
            if (s[start] != s[end]) {
                return false;
            }
            start++; end--;
        }
        return true;
    }

    void backtracking(std::string s, vector<vector<std::string>>& res, vector<std::string>& temp) {
        if (s.size() == 0){
            res.push_back(temp);
            return;
        }
        for (int i=0; i<s.size(); i++) {
            std::string part = s.substr(0, i+1);
            if (isPalindrome(part)) {
                temp.push_back(part);
                backtracking(s.substr(i+1), res, temp);
                temp.pop_back();
            }
        }
    }

    vector<vector<string>> partition(string s) {
        std::vector<vector<string>> res;
        std::vector<string> temp;
        
        backtracking(s, res, temp);

        return res;
    }
};
