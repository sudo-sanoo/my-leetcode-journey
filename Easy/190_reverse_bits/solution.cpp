class Solution {
public:
    void intToBinary(std::vector<int>& b, int n) {
        for (int i=31; i>=0; i--) {
            b[i] = n & 1; // equivalent to n % 2; but faster
            n >>= 1; // equivalent to n /= 1; but faster
        }
    }
    
    int reverseBits(int n) {
        std::vector<int> b(32, 0);
        // no need for reversal here, use a for loop to travel from left to right cleanly to convert the vector to int
        intToBinary(b, n);
        unsigned int res = 0;
        for (int i=0; i<32; i++) {
            int deci = b[i] * std::pow(2, i);
            res += deci;
            // OR
            // if (b[i] == 1)
            //     res |= (1U << i);
        }
        
        return (int)res;
    }
};
