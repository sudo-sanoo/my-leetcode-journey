class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        // nums[0] to nums[p] is always increasing, no equals
        // nums[p] to nums[q] is always decreasing, no equals
        // nums[q] to nums[n-1] is always increasing, no equals
        int p = 0, q = 0, end = 0;

        for (int i=1; i<nums.size(); i++) {
            if ((p == 0) && (q == 1)) {return false;}
            if (nums[i] == nums[i-1]) {return false;}
            if (nums[i] > nums[i-1]) {
                if ((p == 1) && (q == 1)){
                    end = 1;
                }
                p = 1;
            }
            else {
                if (end == 1) {
                    return false;
                }
                q = 1;
            }
        }
        return ((p==1)&&(q==1)&&(end==1));
    }
};
