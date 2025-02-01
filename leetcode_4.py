# 4. Median of Two Sorted Arrays

# https://leetcode.com/problems/median-of-two-sorted-arrays/?envType=problem-list-v2&envId=array s

nums1 = [1,2]
nums2 = [3]

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        combine_num = sorted(nums1 + nums2)
        length = len(combine_num)
        number = ((combine_num[length//2 - 1] + combine_num[length//2]) / 2.0) if length % 2 == 0 else combine_num[length//2]
        return number

output = Solution()
print(output.findMedianSortedArrays(nums1,nums2))
