class Solution:
    _INT_MAX_STR = str(2147483647)
    _INT_MIN_STR = str(-2147483648)
    
    _ref_str = _INT_MIN_STR
    _ref_str_idx = 0
    _check_next = True
    _cmp_result = True
    
    def __init__(self):
        pass
    
    def reverse(self, x):
        x_str = str(x)
        x_str_idx = len(x_str) - 1
        is_pos = x_str[0] != '-'
        
        self._set_ref(x_str)
        
        res = 0
        while x_str_idx >= (0 if is_pos else 1):
            if not self._can_reverse(x_str, x_str_idx):
                return 0
            
            res = res * 10 + int(x_str[x_str_idx])
            x_str_idx -= 1
            
        return res if is_pos else -res
        
    def _set_ref(self, x_str):
        is_pos = x_str[0] != '-'
        if is_pos:
            self._ref_str = self._INT_MAX_STR
            self._ref_str_idx = 0
        else:
            self._ref_str = self._INT_MIN_STR
            self._ref_str_idx = 1
            
    def _can_reverse(self, x_str, x_str_idx):
        if not self._check_next:
            return self._cmp_result
        
        if len(x_str) < len(self._ref_str):
            self._check_next = False
            self._cmp_result = True
            return self._cmp_result
        
        if len(x_str) > len(self._ref_str):
            self._check_next = False
            self._cmp_result = False
            return self._cmp_result
        
        x_digit = int(x_str[x_str_idx])
        ref_digit = int(self._ref_str[self._ref_str_idx])
        self._ref_str_idx += 1
        
        if x_digit < ref_digit:
            self._check_next = False
            self._cmp_result = True
        elif x_digit > ref_digit:
            self._check_next = False
            self._cmp_result = False
        else:
            self._cmp_result = True
            
        return self._cmp_result
