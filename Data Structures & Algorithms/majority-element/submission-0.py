class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen={}
        for i in range(len(nums)):
            if nums[i] in seen.keys():
                seen[nums[i]]+=1
            else:
                seen[nums[i]]=1
        
        return max(seen, key=lambda x: seen[x])