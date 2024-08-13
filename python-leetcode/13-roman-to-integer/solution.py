class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }

        # if s not in roman:
        #     return False

        i = 0
        num = 0

        while i < len(s):
            print(f"indeks i= {i}, s[i:i+2]: {s[i:i+2]}, s[i]: {s[i]}")

            # cek jika ada dua simbol karakter seperti (IV, IX, and another)
            if i + 1 < len(s) and s[i : i + 2] in roman:
                print(f"Ditemukan simbol dua karakter: {s[i:i+2]}")
                num += roman[s[i : i + 2]]
                i += 2

            else:
                print(f"Ditemukan simbol tunggal: {s[i]}")
                num += roman[s[i]]
                # print(roman[s[i]])
                i += 1

            print(f"Total setelah iterasi: {num}\n")

        return num


solution = Solution()
result = solution.romanToInt("MCMXCIV")
print(result)
