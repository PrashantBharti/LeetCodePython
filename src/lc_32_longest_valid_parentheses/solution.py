class Solution:
    def longestValidParentheses(self, s):
        if not s:
            return 0
        
        max_len = 0
        substring_start = -1
        nb_open = 0
        nb_close = 0
        
        for i in range(len(s)):
            if substring_start == -1:
                substring_start = i
            
            if s[i] == '(':
                nb_open += 1
            else:
                nb_close += 1
            
            if nb_open == nb_close:
                max_len = max(max_len, nb_open + nb_close)
            elif nb_close > nb_open:
                nb_open = 0
                nb_close = 0
                substring_start = -1
        
        if nb_open == nb_close:
            return max_len
        
        nb_open = 0
        nb_close = 0
        for i in range(len(s)-1, substring_start, -1):
            if s[i] == '(':
                nb_open += 1
            else:
                nb_close += 1
            
            if nb_open == nb_close:
                max_len = max(max_len, nb_open + nb_close)
            elif nb_open > nb_close:
                nb_open = 0
                nb_close = 0
                
        return max_len     
        