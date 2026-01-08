class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n < 3) { return 0; }
        
        int trapped = 0;
        int L = 0;
        int R = n-1;
        int left_max = 0;
        int right_max = 0;

        while (L < R) {
            left_max = std::max(left_max, height[L]);
            right_max = std::max(right_max, height[R]);

            if (height[L] >= height[R]) {
                int wR = right_max - height[R];
                if (wR < 0) { wR = 0; }
                trapped += wR;
                R--;
            }
            else {
                int wL = left_max - height[L];
                if (wL < 0) { wL = 0; }
                trapped += wL;
                L++;
            }
        }

        return trapped;
    }
};
