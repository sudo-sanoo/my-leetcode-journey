class Solution {
public:
    void remove_lead_trail_spaces(string& s) {
        // remove leading spaces
        int start = 0;
        int end = s.size();
        while (start <= end && s[start] == ' ') {
            start++;
        }
        // remove trailing spaces
        while(start <= end && s[end] == ' ') {
            end--;
        }
        
        if (start > end ) s="";
        else s = s.substr(start, end-start+1);
    }
    
    string reverseWords(string s) {
        remove_lead_trail_spaces(s);
        int idx=0;
        int ptr=s.size()-1;
        std::string res = "";
        while (ptr>=0) {
            while (ptr>=0 && s[ptr] != ' ') {
                res.insert(idx,1,s[ptr]);
                ptr--;
            }
            while (ptr>=0 && s[ptr] == ' ') {
                if (s[ptr-1] != ' ') { 
                    res+=' ';
                    idx = res.size();
                }
                ptr--;
            }
        }
        remove_lead_trail_spaces(res);
        return res;
    }
};
