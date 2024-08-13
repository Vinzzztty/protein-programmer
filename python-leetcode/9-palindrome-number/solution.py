class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        # ## SOLUTION 1
        # # ubah x menjadi string
        # x_str = str(x)

        # print(x_str[::-1])

        # return x_str == x_str[::-1]

        ## SOLUTION 2

        # Palindrom tidak mungkin berakhiran 0 dan negatif
        if x < 0 or (x % 10 == 0 and x != 0):
            print(f"Angka negatif atau berakhiran 0: {x}")
            return False

        # init reversed_half dengan 0
        reversed_half = 0
        print(f"Mulai dengan x: {x}, reversed_half: {reversed_half}")

        # Loop hingga x lebih besar dari reversed_half
        while x > reversed_half:
            print(f"Sebelum iterasi - x: {x}, reversed_half: {reversed_half}")
            reversed_half = reversed_half * 10 + x % 10

            # Hilangkan digit terakhir dari x
            x //= 10
            print(f"Setelah iterasi - x: {x}, reversed_half: {reversed_half}")

        # cek apakah angka asli (x) sama dengan reversed_half
        is_palindrome = x == reversed_half or x == reversed_half // 10
        print(
            f"Final - x: {x}, reversed_half: {reversed_half}, is_palindrome: {is_palindrome}"
        )
        return is_palindrome


solution = Solution()
result = solution.isPalindrome(121)
print(result)
