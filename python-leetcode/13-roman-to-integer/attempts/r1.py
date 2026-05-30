"""Repetition R1 for LeetCode 13: Roman to Integer."""

from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        
        # Define roman into Dictionary
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        results = 0

        for i in range(len(s)):
            curr = roman[s[i]]
            next_val = roman[s[i + 1]] if i + 1 < len(s) else 0

            if curr < next_val:
                results -= curr

            else:
                results += curr

        return results


sol = Solution()
print(sol.romanToInt("IV"))
