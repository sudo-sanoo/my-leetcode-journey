class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        std::vector<int> vertical;
        std::vector<int> horizontal;
        for (int m=0; m<matrix.size(); m++) {
            for (int n=0; n<matrix[0].size(); n++) {
                if (matrix[m][n] == 0) {
                    vertical.push_back(n);
                    horizontal.push_back(m);
                }
            }
        }

        for (int v : vertical) {
            for (int i=0; i<matrix.size(); i++) {
                matrix[i][v] = 0;
            }
        }

        for (int h : horizontal) {
            for (int i=0; i<matrix[0].size(); i++) {
                matrix[h][i] = 0;
            }
        }
    }
};
