from collections import defaultdict

class Solution:
    def getSkyline(self, buildings):
        events = []
        
        for L, R, H in buildings:
            events.append((L, H, 'start'))
            events.append((R, H, 'end'))
        
        events.sort(key=lambda x: (x[0], x[2] == 'end', -x[1] if x[2] == 'start' else x[1]))
        
        result = []
        active_heights = defaultdict(int)
        prev_height = 0
        
        for x, height, event_type in events:
            if event_type == 'start':
                active_heights[height] += 1
            else:
                active_heights[height] -= 1
            
            if active_heights[height] == 0:
                del active_heights[height]
            
            current_height = 0
            if active_heights:
                current_height = max(active_heights.keys())
            
            if current_height != prev_height:
                result.append([x, current_height])
                prev_height = current_height
        
        return result
