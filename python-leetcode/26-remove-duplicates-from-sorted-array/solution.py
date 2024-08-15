class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Inisialisasi 'replace' dengan indeks awal 1
        # Karena indeks 0 dari nums selalu unik
        replace = 1

        # Inisialisasi output list untuk menyimpan elemen unik
        output = [nums[0]]  # Mulai dengan elemen pertama yang selalu unik
        print(f"Start: replace={replace}, output={output}")

        # Loop melalui array mulai dari indeks ke-1
        for i in range(1, len(nums)):
            print(
                f"Checking index {i}: current value={nums[i]}, previous value={nums[i - 1]}"
            )
            # Jika elemen saat ini tidak sama dengan elemen sebelumnya
            if nums[i - 1] != nums[i]:
                nums[replace] = nums[i]  # Ganti elemen di posisi 'replace'
                output.append(nums[i])  # Tambahkan elemen unik ke output
                print(
                    f"Value at index {i} is unique, updating replace index {replace} with value {nums[i]}"
                )
                replace += 1  # Geser posisi 'replace' ke kanan

        print(f"Final output (unique elements): {output}")
        print(f"Final value of 'replace' (number of unique elements): {replace}")

        # Hasil akhir adalah jumlah elemen unik
        return replace


# Contoh penggunaan:
solution = Solution()
result = solution.removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
print(f"Jumlah elemen unik: {result}")
