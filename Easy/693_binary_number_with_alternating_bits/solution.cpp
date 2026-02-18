class Solution {
public:
    bool hasAlternatingBits(int n) {
        int past = 0;
        int flag = 0;
        while (n/2!=0) {
            if (flag && n%2==past) {
                return false;
            }
            past = n%2;
            n /= 2;
            flag = 1;
        }
        if (past == n) return false;
        return true;
    }
};
