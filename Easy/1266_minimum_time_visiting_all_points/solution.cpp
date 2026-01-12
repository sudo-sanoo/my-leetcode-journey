class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int seconds = 0;
        for (int i=1; i < points.size(); i++) {
            int xDiff = points[i][0] - points[i-1][0];
            int yDiff = points[i][1] - points[i-1][1];
            seconds += max(abs(xDiff), abs(yDiff)); 
        }
        return seconds;
    }
};
