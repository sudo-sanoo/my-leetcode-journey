class Solution {
public:
    void increment(std::string& binary) {
        int idx = binary.size()-1;
        while (idx >= 0 && binary[idx] == '1') {
            binary[idx] = '0';
            idx--;
        }
        binary[idx] = '1';
    }
    
    string findDifferentBinaryString(vector<string>& nums) {
        int n = nums.size();
        std::string binary(n, '0');
        std::unordered_set<std::string> st(nums.begin(), nums.end());

        while (st.count(binary)) {
            increment(binary);
        }
        return binary;
    }
};
