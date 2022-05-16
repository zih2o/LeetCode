class Solution:
    def fib(self, n: int) -> int:
        
        x, y = 0, 1
        if n==1:
            return 1
        elif n==0:
            return 0
        
        for i in range(2, n+1):
            x, y = y, x+y
            
        return y