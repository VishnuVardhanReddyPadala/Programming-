class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        
        n, m = len(matrix), len(matrix[0])
        heights = [0] * m
        max_area = 0
        
        for i in range(n):
            for j in range(m):
                heights[j] = heights[j] + 1 if matrix[i][j] == '1' else 0
            
            max_area = max(max_area, self.largestRectangleArea(heights))
        
        return max_area
    
    def largestRectangleArea(self, heights):
        stack = [-1]
        max_area = 0
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = len(heights) - stack[-1] - 1
            max_area = max(max_area, height * width)
        
        return max_area
