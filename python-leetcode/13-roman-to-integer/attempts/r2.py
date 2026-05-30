"""Repetition R2 for LeetCode 13: Roman to Integer."""

from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        results = 0

        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                results -= roman[s[i]]

            else:
                results += roman[s[i]]

        return results + roman[s[-1]]


sol = Solution()
print(sol.romanToInt("XI"))
