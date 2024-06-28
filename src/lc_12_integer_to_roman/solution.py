class Solution:
    def intToRoman(self, num):
        result = ''
        sym = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        val = [1000, 900, 500,  400, 100,   90,  50,   40,  10,    9,   5,    4,   1]
        
        for i in range(len(sym)):
            while num >= val[i]:
                num -= val[i]
                result += sym[i]
                
        return result
