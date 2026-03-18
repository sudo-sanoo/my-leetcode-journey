class Solution {
public:
    int minimumLength(string s) {
        // remove prefix and suffix where: non-empty prefix == non-empty suffix
        // prefix and suffix length dont need to be the same
        // return minimum length of s

        int l = 0;
        int r = s.size()-1;

        while (l < r && s[l] == s[r]) {
            char x = s[l];
            while (l<=r && s[l] == x) {
                l++;
            }
            while (r>l && s[r] == x) {
                r--;
            }
        }

        return r-l+1;
    }
};
