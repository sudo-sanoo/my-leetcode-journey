class Solution {
public:
    int countBinarySubstrings(string s) {
        std::vector<int> group(1, 1);
        char past = s[0];
        int idx = 0;
        for (int i=1; i<s.size(); i++) {
            if (s[i] != past) {
                group.push_back(1);
                idx += 1;
                past = s[i];
            }
            else {
                group[idx] += 1;
            }
        }

        int res=0;
        for (int i=0; i<group.size()-1; i++) {
            res += min(group[i], group[i+1]);
        }

        return res;
    }
};
