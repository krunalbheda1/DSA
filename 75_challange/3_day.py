#3105. Longest Strictly Increasing or Strictly Decreasing Subarray

class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = inc =dec =1
        for i in range(1,len(nums)):
            if( nums[i] > nums[i-1]):
                inc += 1
                dec = 1
            elif( nums[i] < nums[i-1]):
                dec += 1
                inc = 1
            else:
                inc = dec = 1
            max_num = max(max_num,inc,dec)
        return max_num


        