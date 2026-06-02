"""Repetition R2 for LeetCode 9: Palindrome Number."""

# Brute Force Solution


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        rev = 0

        while x > 0:
            digit = x % 10
            rev = rev * 10 + digit
            x //= 10

        return original == rev


sol = Solution()
print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(112))
print(sol.isPalindrome(1231))
