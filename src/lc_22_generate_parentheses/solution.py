class Solution:
    def generateParenthesis(self, n):
        res = []
        if not n:
            return res
        
        str = []
        self._generate_parenthesi_recursive(n, n, str, res)
        return res
    
    def _generate_parenthesi_recursive(self, nb_open, nb_close, str, res):
        if nb_open == 0 and nb_close == 0:
            res.append(''.join(str))
            return
        
        if not str:
            self._operate('(', nb_open, nb_close, str, res)
            return
        
        if nb_open > 0:
            self._operate('(', nb_open, nb_close, str, res)
            
        if nb_close > nb_open:
            self._operate(')', nb_open, nb_close, str, res)
            
    def _operate(seff, ch, nb_open, nb_close, str, res):
        if ch == '(':
            nb_open -= 1
        else:
            nb_close -= 1
            
        str.append(ch)
        seff._generate_parenthesi_recursive(nb_open, nb_close, str, res)        
        str.pop()
        
        if ch == '(':
            nb_open += 1
        else:
            nb_close += 1
