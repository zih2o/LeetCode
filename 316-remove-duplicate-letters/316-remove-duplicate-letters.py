class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        result, counter = [], collections.Counter(s)
        
        for char in s:
            counter[char] -= 1
            if char in result:
                continue
            while result and char < result[-1] and counter[result[-1]] > 0:
                result.pop()
            result.append(char)
            
        return ''.join(result)
            