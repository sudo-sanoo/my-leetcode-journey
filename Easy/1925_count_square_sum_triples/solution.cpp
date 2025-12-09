#include <cmath>
#include <iomanip>
class Solution {
public:
    int countTriples(int n) {
        int cnt = 0;
        for (int a=1; a<=n; a++){
            for (int b=a; b<=n; b++){
                int c_squared = a*a + b*b;
                int c = static_cast<int>(std::sqrt(c_squared));
                if (c<=n && c*c==c_squared){
                    if (a != b){
                        cnt += 2;
                    }
                    else {
                        cnt += 1;
                    }
                }
            }
        }
        return cnt;
    }
};
