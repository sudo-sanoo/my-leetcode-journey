class Solution {
public:
    int minLengthAfterRemovals(string s) {
        int cnt_a = 0;
        int cnt_b = 0;
        for (char c : s) {
            if (c == 'a') cnt_a += 1;
            else cnt_b += 1;
        }

        if (cnt_a == cnt_b) return 0;
        if (cnt_a == 0 || cnt_b == 0) return cnt_a + cnt_b;

        return abs(cnt_a - cnt_b);
    }
};
