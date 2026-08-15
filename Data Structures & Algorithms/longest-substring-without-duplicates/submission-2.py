class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        best = 0

        for i in range(len(s)):
            seen = set()

            for j in range(i, len(s)):

                if s[j] in seen:
                    break

                seen.add(s[j])

                best = max(best, len(seen))

        return best
        '''
        best = 0
        left = 0
        seen = set()

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left+=1

            seen.add(s[right])

            best = max(best, right-left+1)

        return best
            
