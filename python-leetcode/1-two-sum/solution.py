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
            selisih  = target - num

            # Cek apakah selisih sudah ada dalam dictionary
            if selisih in seen:
                return [seen[selisih], i]

            seen[num] = i
        
        return []
        
        # i = 0
        # while i < len(nums):
        #     temp = nums[i] + nums[i+1]
        #     if temp == target:
        #         print(nums[i])
        #     i += 1 
        