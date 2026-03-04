class Solution {
public:
    int binary_search(vector<int>& nums, int left, int right, int target) {
        int l = left;
        int r = right;
        while (l<=r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] == target)
                return mid;
            else if (nums[mid] > target)
                r = mid-1;
            else
                l = mid + 1;
        }
        return -1;
    }

    int search(vector<int>& nums, int target) {
        // O(log n) solution
        int pivot_idx = 0;
        int l = 0;
        int r = nums.size()-1;
        while (l<r) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[r]) {
                pivot_idx = mid;
                l = mid+1;
            }
            else r = mid;
        }
        
        int res = binary_search(nums, 0, pivot_idx, target);
        if (res != -1) return res;

        return binary_search(nums, pivot_idx+1, nums.size()-1, target);
    }
};
