class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        volume = 0
        left_max, right_max = height[left], height[right]
        
        if not height:
            return volume
            
        while left < right:
            left_max = max(height[left], left_max)
            right_max = max(height[right], right_max)
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
                    
            
            