class Solution(object):
    def isNumber(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        s = s.strip()
        if s.lower() in {\inf\, \infinity\, \nan\, \-inf\, \+inf\, \-infinity\, \+infinity\, \-nan\, \+nan\}:
            return False
        
        try:
            float(s)
            return True
        except ValueError:
            return False
