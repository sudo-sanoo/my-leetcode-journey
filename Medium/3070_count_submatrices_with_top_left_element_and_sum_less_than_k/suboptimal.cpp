class Solution {
public:
    int countSubmatrices(vector<vector<int>>& grid, int k) {
        int rows = grid.size(), cols = grid[0].size();
        std::vector<std::vector<long long>> matrix(rows);
        // reconstruct matrix to store long long (constraints: 1 <= k <= 10^9)
        for (int i=0; i<rows; i++) {
            matrix[i] = std::vector<long long>(grid[i].begin(), grid[i].end());
        }

        // compute horizontally
        for (int r=0; r<rows; r++) {
            for (int c=0; c<cols; c++) {
                if (c > 0) 
                    matrix[r][c] += matrix[r][c-1];
            }
        }

        // compute vertically
        for (int c=0; c<cols; c++) {
            for (int r=0; r<rows; r++) {
                if (r > 0)
                    matrix[r][c] += matrix[r-1][c];
            }
        }

        // iterate the new matrix and find the number of submatrices
        int res = 0;
        for (int r=0; r<rows; r++) {
            for (int c=0; c<cols; c++) {
                if (matrix[r][c] <= k)
                    res++;
                else
                    break;
            }
        }

        return res;
    }
};
