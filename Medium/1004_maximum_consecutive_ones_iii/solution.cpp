class Solution {
public:
    int longestOnes(vector<int>& nums, int k) {
        int l = 0, res = 0;
        int zero_count = 0;
        for (int r=0; r<nums.size(); r++) {
            if (nums[r] == 0) zero_count++;
            while (zero_count > k) {
                if (nums[l] == 0) zero_count--;
                l++;
            }
            res = max(r-l+1, res);
        }
        return res;
    }
};
