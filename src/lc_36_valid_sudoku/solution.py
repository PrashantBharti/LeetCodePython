class Solution:
    def isValidSudoku(self, board):
        if not board or not board[0]:
            return False
        
        map = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue

                num = board[r][c]
                r_k = self._get_row(r, c)
                c_k = self._get_col(r, c)
                b_k = self._get_box(r, c)
                k = None
                
                if board[r][c] in map:
                    k = map[board[r][c]]
                    if r_k in k or c_k in k or b_k in k:
                        return False
                else:
                    k = set()
                
                k.add(r_k)
                k.add(c_k)
                k.add(b_k)
                map[num] = k
                
        return True
        
    def _get_row(self, r, c):
        return ''.join(['R', str(r)])
    
    def _get_col(self, r, c):
        return ''.join(['C', str(c)])
    
    def _get_box(self, r, c):
        return ''.join(['B', str((r // 3) * 3 + c // 3)])