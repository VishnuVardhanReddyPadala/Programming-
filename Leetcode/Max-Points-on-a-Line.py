from collections import defaultdict

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        result = 0
        for i in range(len(points)):
            same = 1
            lines = defaultdict(int)
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx = x2 - x1
                dy = y2 - y1
                if dx == 0 and dy == 0:
                    same += 1
                    continue
                g = gcd(dx, dy)
                dx //= g
                dy //= g
                lines[(dx, dy)] += 1
            max_line = 0
            for count in lines.values():
                if count > max_line:
                    max_line = count
            result = max(result, same + max_line)
        return result
