class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        maxFreq = 0
        best = 0

        for right in range(len(s)):
            
            if s[right] in count:
                count[s[right]]+=1
            else:
                count[s[right]]=1

            maxFreq = max(count.values())

            while (right - left + 1) - maxFreq > k:
                count[s[left]]-=1
                left+=1
            
            best = max(best, right-left+1)

        return best
                
        
