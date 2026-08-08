class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup = []
        flag = False
        for _ in nums:
            if _ not in dup:
                dup.append(_)
            else:
                flag = True
                break

        return flag