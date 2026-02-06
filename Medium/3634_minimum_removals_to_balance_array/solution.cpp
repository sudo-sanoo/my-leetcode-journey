class Solution {
public:
    int minRemoval(vector<int>& nums, int k) {
        int n = nums.size();
        if (n==1) return 0;
        std::sort(nums.begin(), nums.end());
        int length = 0;
        int sw = 0;
        int l = 0;
        for (int r=1; r<n; r++) {
            while (nums[r] > ((long long)nums[l]*k)) l++; // (1LL*nums[l]*k) also works
            length = r-l+1;
            sw = max(length, sw);
        }
        return n - sw;
    }
};
