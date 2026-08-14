class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        water = 0
        n = len(height)
        
        while i < n-1:
            left = i
            right = -1
            best = i + 1

            for j in range(i+1,n):
                
                if height[j] >= height[left]:
                    right = j
                    break

                if height[j] > height[best]:
                    best = j

            if right == -1:
                right = best
                
            level = min(height[left], height[right])

            for k in range(left+1, right):
                water += level - height[k]

            i = right

        return water
