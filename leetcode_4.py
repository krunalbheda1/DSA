nums1 = [1,3]
nums2 = [2,4]
# Output: 2.00000

combine_nums = sorted(nums1 + nums2)
len_num =len(combine_nums)

print(combine_nums)

mid = len_num//2
print(mid)

if (len_num % 2 != 0):
    print(combine_nums[mid])
else:
    print(float(combine_nums[mid] + combine_nums[mid-1]) )

