class Solution:
    def climbStairs(self, n: int) -> int:
        a = 0
        b = 1
        for _ in range(n):
            a_temp = a
            a = b
            b = a_temp + b
        return b