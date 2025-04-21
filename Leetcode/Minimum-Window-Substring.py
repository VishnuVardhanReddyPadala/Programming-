class Solution(object):
    def minWindow(self, s, t):
        \\\
        :type s: str
        :type t: str
        :rtype: str
        \\\
        if not s or not t:
            return \\
        
        t_freq = {}
        for char in t:
            t_freq[char] = t_freq.get(char, 0) + 1
        
        s_freq = {}
        left = 0
        min_len = float('inf')
        min_substr = \\
        count = len(t)
        
        for right in range(len(s)):
            char = s[right]
            s_freq[char] = s_freq.get(char, 0) + 1
            
            if char in t_freq and s_freq[char] <= t_freq[char]:
                count -= 1
            
            while count == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_substr = s[left:right+1]
                
                s_freq[s[left]] -= 1
                if s[left] in t_freq and s_freq[s[left]] < t_freq[s[left]]:
                    count += 1
                left += 1
        
        return min_substr
