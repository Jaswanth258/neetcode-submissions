class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        need = {}
        window = {}

        for ch in t:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1

        
        have = 0
        needCount = len(need)

        left = 0

        resLen = float('inf')
        res = [-1, -1]


        for right in range(len(s)):

            ch = s[right]

            if ch in window:
                window[ch] += 1
            else:
                window[ch] = 1

            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == needCount:

                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1

                left += 1


        l, r = res



        return s[l:r+1]
                