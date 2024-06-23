class Solution:
    def __init__(self):
        pass
    
    def longestPalindrome(self, input):
        lps = ""
        lps_len = 0
        
        for i in range(len(input)):
            l, r = i, i
            while l >= 0 and r < len(input) and input[l] == input[r]:
                if (r - l + 1) > lps_len:
                    lps = input[l:r+1]
                    lps_len = r - l + 1
                l -= 1
                r += 1

            l, r = i, i + 1
            while l >= 0 and r < len(input) and input[l] == input[r]:
                if (r - l + 1) > lps_len:
                    lps = input[l:r+1]
                    lps_len = r - l + 1
                l -= 1
                r += 1
                
        return lps
