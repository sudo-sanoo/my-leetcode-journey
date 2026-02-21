class Solution {
public:
    int countPrimeSetBits(int left, int right) {
        //64-bit system, an int has at most 63 ones
        const std::unordered_set<int> PRIMES = {
            2,3,5,7,11,13,17,19,23,29,31,
            37,41,43,47,53,59,61
        };
        int res=0;
        for (int x=left; x<=right; x++) {
            int tmp=x;
            // Brian Kernighan's Algorithm
            // count number of 1s
            int cnt = 0;
            while (tmp != 0) {
                tmp &= (tmp-1);
                cnt++;
            }
            if (PRIMES.count(cnt)) res++;
        }
        return res;
    }
};
