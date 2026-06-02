"""Repetition R1 for LeetCode 9: Palindrome Number."""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #Handling Palindrom negative value, Karena negative sudah pasti bukan palindrome
        if x < 0:
            return False
        
        s = str(x)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
        
sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))
print(sol.isPalindrome(1231))
