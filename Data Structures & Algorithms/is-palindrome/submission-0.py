class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1
        while i < j:
            if not self.is_alpha_numeric2(s[i]):
                i += 1
                continue
            if not self.is_alpha_numeric(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -=1
        return True

    def is_alpha_numeric(self, c: str) -> bool:
        return c.isalnum()
    
    def is_alpha_numeric2(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))