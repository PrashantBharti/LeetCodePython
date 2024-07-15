class Solution:
    def solveSudoku(self, board):
        if not board or not board[0]:
            return
        
        self._solve(board)
    
    def _solve(self, board):
        r = -1
        c = -1
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    r = i
                    c = j
                    break

            if r != -1 and c != -1:
                break
            
        if r == -1 or c == -1:
            return True
        
        for k in range(10):
            board[r][c] = str(k)
            
            if not self._is_row_valid(board, r, c) or not self._is_col_valid(board, r, c) or not self._is_box_valid(board, r, c):
                continue
            
            if self._solve(board):
                return True
        
        board[r][c] = "."
        return False
    
    def _is_row_valid(self, board, r, c):
        seen = set()
        for i in range(9):
            if board[r][i] == ".":
                continue
            
            if board[r][i] in seen:
                return False
            
            seen.add(board[r][i])
            
        return True
    
    def _is_col_valid(self, board, r, c):
        seen = set()
        for i in range(9):
            if board[i][c] == ".":
                continue

            if board[i][c] in seen:
                return False

            seen.add(board[i][c])
            
        return True
    
    def _is_box_valid(self, board, r, c):
        seen = set()
        r = 3 * (r // 3)
        c = 3 * (c // 3)
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j] == ".":
                    continue

                if board[i][j] in seen:
                    return False

                seen.add(board[i][j])
                
        return True