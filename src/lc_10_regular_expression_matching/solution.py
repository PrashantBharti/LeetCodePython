class Solution:
    def isMatch(self, s, p):
        return self._is_match(s, p, 0, 0)
        
    def _is_match(self, s, p, i, j):
        if i >= len(s) and j >= len(p):
            return True
        
        if j >= len(p):
            return False
        
        match = i < len(s) and (s[i] == p[j] or p[j] == '.')
        if (j + 1) < len(p) and p[j + 1] == '*':
            return (match and self._is_match(s, p, i + 1, j)) or self._is_match(s, p, i, j + 2)
        
        if match:
            return self._is_match(s, p, i + 1, j + 1)
        
        return False
