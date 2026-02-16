class Solution {
public:
    string convert(string s, int numRows) {
        if ((numRows == 1) || (numRows >= s.size())) return s;
        int row = 0;
        int diag = 1;
        std::vector<std::string> v(numRows, "");
        for (char ch : s) {
            v[row] += ch;

            if (row==0)
                diag=1;
            else if (row == numRows-1)
                diag=-1;
            
            row+=diag;
        }

        std::string res = "";
        for (std::string st : v) {
            res += st;
        }

        return res;
    }
};
