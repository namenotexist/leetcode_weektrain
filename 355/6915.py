from typing import List
class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        n = len(nums)
        new_nums = [nums[n-1]]
        for i in range(n-2, -1, -1):
            if new_nums[-1] >= nums[i]:
                tmp = new_nums.pop()
                new_nums.append(tmp + nums[i])
            else:
                new_nums.append(nums[i])
        return max(new_nums)

        