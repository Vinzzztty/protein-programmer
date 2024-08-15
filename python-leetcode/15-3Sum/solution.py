class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # Target adalah 0
        target = 0

        # Urutkan array terlebih dahulu
        nums.sort()
        print(f"Sorted nums: {nums}")

        # Inisialisasi set untuk menyimpan triplet unik
        # Set digunakan untuk mencegah duplikasi
        s = set()
        output = []

        # Iterasi melalui array dengan variabel i
        for i in range(len(nums)):
            # Debug: Melihat indeks dan nilai saat ini
            print(f"Processing index {i} with value {nums[i]}")

            # Inisialisasi dua pointer, j dan k
            j = i + 1
            k = len(nums) - 1

            # Loop untuk mencari triplet yang jumlahnya sama dengan target (0)
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                print(
                    f"Checking triplet: ({nums[i]}, {nums[j]}, {nums[k]}) with sum: {sum}"
                )

                if sum == target:
                    s.add((nums[i], nums[j], nums[k]))
                    print(
                        f"Triplet found and added to set: ({nums[i]}, {nums[j]}, {nums[k]})"
                    )
                    j += 1
                    k -= 1

                # Jika jumlah lebih kecil dari target, geser pointer j ke kanan
                elif sum < target:
                    print(f"Sum {sum} is less than target {target}. Incrementing j.")
                    j += 1

                # Jika jumlah lebih besar dari target, geser pointer k ke kiri
                else:
                    print(f"Sum {sum} is greater than target {target}. Decrementing k.")
                    k -= 1

        # Ubah set menjadi list untuk mengembalikan hasil akhir
        output = list(s)
        print(f"Final set of unique triplets: {output}")
        return output


# Contoh penggunaan:
solution = Solution()
result = solution.threeSum(nums=[-1, 0, 1, 2, -1, -4])
print(f"Triplets that sum to 0: {result}")
