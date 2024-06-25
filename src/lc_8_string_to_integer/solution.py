class Solution:
    def myAtoi(self, s):
        s = s.strip()
        if not s:
            return 0
        sign = -1 if s[0] == '-' else 1
        if s[0] in ('-', '+'):
            s = s[1:]
        i = 0
        while i < len(s) and s[i].isdigit():
            i += 1
        try:
            ret = sign * int(s[:i])
        except ValueError:
            ret = 0
        return min(max(ret, -2**31), 2**31 - 1)
