from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Build Map
        hashmap = {}

        for i in range(len(nums)):
            hashmap[nums[i]] = i

        hashmap_map = hashmap
        print(hashmap_map)

        # Find the pair from complement
        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]

        return []


sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 18))
