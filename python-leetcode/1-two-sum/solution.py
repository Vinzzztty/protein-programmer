class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        # dictionary untuk menyimpan selisih index
        seen = {}

        for i, num in enumerate(nums):

            # Hitung selisih antara target dan angka saat ini
            selisih = target - num
            print(selisih)

            # Cek apakah selisih sudah ada dalam dictionary
            if selisih in seen:
                return [seen[selisih], i]

            seen[num] = i

        return []


solution = Solution()
nums = [1, 2, 6, 7]
result = solution.twoSum(nums, 9)
print(result)
