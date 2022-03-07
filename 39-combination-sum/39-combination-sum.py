class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        
        def dfs(elements, start:int, now: int):
            if now == target:
                results.append(elements[:])
                return
            elif now >target:
                return
            else:
                for i in range(start, len(candidates)):
                    elements.append(candidates[i])
                    dfs(elements, i, now + candidates[i])
                    elements.pop()
        dfs([], 0, 0)
        return results