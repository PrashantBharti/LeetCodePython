class Solution:
    _num_rows = None
    _dir = None
    _cur_row = None
    
    def __init__(self):
        pass
    
    def convert(self, input, numRows):
        if not input or numRows < 1:
            return ''
        
        self._initialize(numRows)
        grid = ['' for _ in range(numRows)]
        for c in input:
            cur_row = self._get_next_row()
            grid[cur_row] += c
            
        return ''.join(grid)
    
    def _initialize(self, num_rows):
        self._num_rows = num_rows
        self._dir = 0
        self._cur_row = -1
        
    def _get_next_row(self):
        if self._num_rows == 1:
            return 0
        
        if self._dir == 0:
            self._cur_row += 1
            if self._cur_row == self._num_rows - 1:
                self._dir = 1
        else:
            self._cur_row -= 1
            if self._cur_row == 0:
                self._dir = 0

        return self._cur_row
