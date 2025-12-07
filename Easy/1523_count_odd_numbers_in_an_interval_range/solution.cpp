class Solution {
public:
    int countOdds(int low, int high) {
        int n = (high-low)/2;
        return (low % 2 == 0 and high % 2 == 0) ? n : n+1;
    }
};
