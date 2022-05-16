class Solution:
    def fib(self, n: int) -> int:
        
        Fn = collections.defaultdict(int)
        
        Fn[0] = 0
        Fn[1] = 1
        
        for i in range(2, n+1):
            Fn[i] = Fn[i-1] + Fn[i-2]
            
        return Fn[n]