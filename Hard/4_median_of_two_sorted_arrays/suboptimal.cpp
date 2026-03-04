class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        std::vector<int> v;
        for (int x : nums1) {
            v.push_back(x);
        }
        for (int y : nums2) {
            v.push_back(y);
        }
        
        if (v.size() == 1) return v[0];

        std::sort(v.begin(), v.end());

        bool odd = v.size() % 2;

        int l = 0;
        int r = v.size()-1;
        int median = l + (r - l) / 2;
        if (!odd)
            return (v[median] + v[median+1]) / 2.0;
        
        return v[median];
    }
};
