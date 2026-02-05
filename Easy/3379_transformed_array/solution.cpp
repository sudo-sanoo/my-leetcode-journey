class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        vector<int> res;
        int n = nums.size();
        for (int i=0; i<n; i++) {
            if (nums[i] == 0) res.push_back(nums[i]);
            else if (nums[i] < 0) {
                res.push_back(nums[(((i-abs(nums[i])) % n) + n) % n]);
            }
            else {
                res.push_back(nums[(i + nums[i]) % n]);
            }
        }
        return res;
        /*
        vector<int> res;
        int n = nums.size();
        int idx = 0;
        for (int i=0; i<n; i++) {
            if (nums[i] == 0) res.push_back(nums[i]);
            else if (nums[i] < 0) {
                idx = i - abs(nums[i]);
                while (idx < 0) {
                    idx += n;
                }
                res.push_back(nums[idx]);
            }
            else {
                idx = i + nums[i];
                while (idx > n-1) {
                    idx -= n;
                }
                res.push_back(nums[idx]);
            }
        }

        return res;
        */
    }
};class Solution {
public:
    vector<int> constructTransformedArray(vector<int>& nums) {
        vector<int> res;
        int n = nums.size();
        for (int i=0; i<n; i++) {
            if (nums[i] == 0) res.push_back(nums[i]);
            else if (nums[i] < 0) {
                res.push_back(nums[(((i-abs(nums[i])) % n) + n) % n]);
            }
            else {
                res.push_back(nums[(i + nums[i]) % n]);
            }
        }
        return res;
        /*
        vector<int> res;
        int n = nums.size();
        int idx = 0;
        for (int i=0; i<n; i++) {
            if (nums[i] == 0) res.push_back(nums[i]);
            else if (nums[i] < 0) {
                idx = i - abs(nums[i]);
                while (idx < 0) {
                    idx += n;
                }
                res.push_back(nums[idx]);
            }
            else {
                idx = i + nums[i];
                while (idx > n-1) {
                    idx -= n;
                }
                res.push_back(nums[idx]);
            }
        }

        return res;
        */
    }
};
