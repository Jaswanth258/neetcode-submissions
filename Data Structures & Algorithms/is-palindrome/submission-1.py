class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''

        clean = ""

        for ch in s:
            if ch.isalnum():
                clean += ch.lower()

        if clean == clean[::-1]:
            return True
        else:
            return False

        '''

        left  = 0
        right = len(s)-1

        while left<right:
            while left < right and  not s[left].isalnum():
                left += 1
            while left < right and  not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            
            left  += 1
            right -= 1 
            
        return True

