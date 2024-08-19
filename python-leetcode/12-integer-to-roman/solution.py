class Solution(object):
    def intToRoman(self, num):

        # Initialize an empty string called Roman to store the resulting Roman numeral.
        roman = ""

        # Create a vector of pairs called storeIntRoman, to store the Roman numeral values and their corresponding symbols.
        storeIntRoman = [
            [1000, "M"],
            [900, "CM"],
            [500, "D"],
            [400, "CD"],
            [100, "C"],
            [90, "XC"],
            [50, "L"],
            [40, "XL"],
            [10, "X"],
            [9, "IX"],
            [5, "V"],
            [4, "IV"],
            [1, "I"],
        ]

        # iterate through storeIntRoman vector using a loop
        for i in range(len(storeIntRoman)):

            # Check if the input integer is greater than or equal to the roman numeral value
            while num >= storeIntRoman[i][0]:
                # add symbol to the roman string and subtract the corresponding value
                roman += storeIntRoman[i][1]
                num -= storeIntRoman[i][0]

        return roman


solution = Solution()
result = solution.intToRoman(num=3749)
print(result)
