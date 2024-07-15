class Solution:
    def countAndSay(self, n):
        if not n or n < 1:
            return ""
        
        if n == 1:
            return "1"
        
        cur_count = 0
        cur_num = None
        result = self.countAndSay(n - 1)
        res = ""
        
        for ch in result:
            if cur_num is None:
                cur_num = ch
                cur_count += 1
            elif ch == cur_num:
                cur_count += 1
            else:
                res += str(cur_count) + cur_num
                cur_num = ch
                cur_count = 1
        
        res += str(cur_count) + cur_num
        return res