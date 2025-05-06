class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        area1 = (C - A) * (D - B)
        area2 = (G - E) * (H - F)
        
        overlap_x = max(0, min(C, G) - max(A, E))
        overlap_y = max(0, min(D, H) - max(B, F))
        
        overlap_area = overlap_x * overlap_y
        
        return area1 + area2 - overlap_area
