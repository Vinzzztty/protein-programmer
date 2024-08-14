class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        # Dapatkan ukuran list string
        size = len(strs)
        print(f"Jumlah string dalam List: {size}")

        # Kondisi tertentu
        if size == 0:
            print("List string kosong")
            return ""

        if size == 1:
            print(f"Hanya ada satu string dalam list: {strs[0]}")
            return strs[0]

        # Sortir list string secara alfabet
        strs.sort()
        print(f"List string setelah diurutkan: {strs}")

        # Ambil string pertama dalam list sebagai base untuk perbandingan
        base = strs[0]
        print(f"Kata dasar (base): {base}")

        # Iterasi pengecekan
        for i in range(len(base)):
            # Iterasi string lain dalam list atau list[i+1]
            for word in strs[1:]:
                print(
                    f"Membandingkan kata: {word}, karakter ke-{i} ({word[i]} dengan base '{base[i]})"
                )

                # Jika karakter (char) tidak cocok atau sudah mencapai akhir salah satu kata
                if i == len(word) or word[i] != base[i]:
                    return base[0:i]

        print(f"Seluruh 'base' adalah prefix umum, return base: '{base}'")
        return base


solution = Solution()
result = solution.longestCommonPrefix(["flower", "flow", "flight"])
print(f"Prefix umum terpanjang adalah: '{result}'")
