class Solution {
public:
    int countCompleteSubarrays(vector<int>& nums) {
        int res = 0;

        std::set<int> freq;
        for (int i=0; i<nums.size(); i++) {
            freq.insert(nums[i]);
        }

        for (int i=0; i<nums.size(); i++) {
            std::set<int> running;
            for (int j=i; j<nums.size(); j++) {
                running.insert(nums[j]);
                if (running == freq) res++;
            }
        }

        return res;
    }
};
