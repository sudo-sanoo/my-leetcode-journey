class Solution {
public:
    long long maxMatrixSum(vector<vector<int>>& matrix) {
        // im pretty sure to get the absolute max, there are two scenarios:
        //  1. if there is an even number of negatives, we can turn every negatives to positive
        //  2. if there is an odd number of negatives,
        //        find minimum absolute value in the entire matrix,
        //        then take the entire sum of the matrix, and sum - 2*(minimum absolute value)
        long long res = 0;
        int negativeCount = 0;
        int absVal;
        long long minimumAbsoluteValue = LLONG_MAX;
        size_t matLen = matrix.size();
        size_t arrLen = matrix[0].size();

        for (int i=0; i<matLen; i++) {
            for (int j=0; j<arrLen; j++){
                absVal = std::abs(matrix[i][j]);
                if (absVal < minimumAbsoluteValue) {
                    minimumAbsoluteValue = absVal;
                }
                if (matrix[i][j] < 0) {
                    negativeCount++;
                    res -= matrix[i][j];
                    continue;
                }
                res += matrix[i][j];
            }
        }

        if (negativeCount % 2 == 1) {
            res -= (2*minimumAbsoluteValue);
        }

        return res;        
    }
};
