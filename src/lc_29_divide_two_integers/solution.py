class Solution:
    def divide(self, dividend, divisor):
        sign = 1 if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0) else -1
        
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        for i in range(31, -1, -1):
            if (dividend >> i) - divisor >= 0:
                ans += 1 << i
                dividend -= divisor << i
        ans = sign*ans
        return min(max(-2147483648, ans), 2147483647)