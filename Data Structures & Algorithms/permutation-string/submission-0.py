class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)

        for i in range(l2):
            if sorted(list(s1))==sorted(list(s2[i:i+l1])):
                return True

        return False