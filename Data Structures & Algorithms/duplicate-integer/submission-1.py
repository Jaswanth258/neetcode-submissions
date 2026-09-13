class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup=[]
        flag = False
        for _ in nums:
            if _ in dup:
                flag = True
            dup.append(_)
        return flag 