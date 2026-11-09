class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
            
        max_len = 1
        now_len = 1

        # [2,3,4,4,5,10,20]
        #                i
        # max_len = 4
        # now_len = 1
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i] - 1:
                now_len += 1
            elif nums[i-1] == nums[i]:
                pass
            else:
                now_len = 1

            max_len = max(max_len, now_len)

        return max_len