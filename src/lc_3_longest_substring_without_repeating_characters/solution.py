class Solution:
    def __init__(self):
        pass
    
    def lengthOfLongestSubstring(self, input):
        if not input:
            return 0
        
        map = {}
        start = 0
        map[input[start]] = start
        
        max_len = 1
        for end in range(1, len(input)):
            c = input[end]
            
            if c in map:
                i = map[c]
                del map[c]
                start = max(start, i + 1)
                
            map[c] = end
            max_len = max(max_len, end - start + 1)
            
        return max_len
    