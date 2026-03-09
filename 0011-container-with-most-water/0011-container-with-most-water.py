class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height)-1
        while left<right:
            area = min(height[left], height[right]) * (right-left)
            maxArea = max(area, maxArea)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return maxArea
