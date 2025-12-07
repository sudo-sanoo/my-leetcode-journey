class Solution:
    def countCollisions(self, directions: str) -> int:
        # Intuition: 
        #   - any leftside cars moving leftwards are going outbound
        #   - any rightside cars moving rightwards are going outbound
        #   - any other cars going towards the middle are eventually going to collide once
        #   - since collision -> stationary, and stationary cars colliding with moving cars = 1 collision, dont count stationary cars
        # remove leading "L"s
        # remove trailing "R"s
        return len(directions.lstrip("L").rstrip("R")) - directions.count("S")
