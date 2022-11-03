class Solution:
    def reverse(self, x: int) -> int:
        arr = list(str(x))
        arr[::] = arr[::-1]
        while len(arr) > 1 and arr[0] == "0":
            arr.pop(0)
        if arr[-1] == "-":
            arr.pop()
            ans = "-" + "".join(arr)
        else:
            ans = "".join(arr)
            
        ans = int(ans)
        return ans if (-2**31 <= ans and ans <= 2**31 - 1) else 0 
        