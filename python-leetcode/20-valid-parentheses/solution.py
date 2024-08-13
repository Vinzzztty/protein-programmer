class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for bracket in s:
            print(f"Memproses bracket: {bracket}")

            # Jika bracket adalah open bracket
            if bracket in pairs:
                stack.append(bracket)
                print(
                    f"Open Bracket '{bracket}' ditambahkan ke stack. Stack saat ini: {stack}"
                )

            # Jika bracket adalah closed bracket
            else:
                # Cek apakah stack kosong atau pasangan tidak cocok
                if len(stack) == 0:
                    print(
                        f"Closed Bracket: '{bracket}' tanpa pasangan yang sesuai. Mengembalikan nilai False"
                    )
                    return False

                last_open = stack.pop()
                if bracket != pairs[last_open]:
                    print(
                        f"Closed bracket '{bracket}' tidak cocok dengan '{last_open}'"
                    )
                    return False

                else:
                    print(
                        f"Closed Bracket '{bracket}' cocok dengan {last_open}. Stack saat ini: {stack}"
                    )

        # Periksa apakah semua bracket dibuka dan ditutup dengan benar
        if len(stack) == 0:
            print(f"Semua bracket telah ditutup. Mengembalikan True.")
            return True
        else:
            print(f"Terdapat bracket yang belum ditutup: {stack}. Mengembalikan False.")
            return False


solution = Solution()
result = solution.isValid("()]{}")
print(result)
