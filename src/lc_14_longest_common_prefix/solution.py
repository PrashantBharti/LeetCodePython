class Solution:
    def longestCommonPrefix(self, strs):
        idx = 0
        flag = True
        
        while flag:
            ch = None
            for str in strs:
                if  idx >= len(str):
                    flag = False
                    break
                
                if ch is None:
                    ch = str[idx]
                elif ch != str[idx]:
                    flag = False
                    break
            
            if flag:
                idx += 1
                
        return strs[0][:idx]
