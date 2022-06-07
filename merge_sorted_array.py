nums1=[4,5,6,0,0,0]
m=3
nums2=[1,2,3]
n=3
# while n>0:
#     if m > 0 and nums1[m-1] > nums2[n-1]:
#         nums1[m+n-1] = nums1[m-1]
#         m -= 1
#     else:
#         nums1[m+n-1] = nums2[n-1]
#         n -= 1
#
# print(nums1)

while n > 0 and m > 0:
    if nums1[m - 1] > nums2[n - 1]:
        nums1[m + n - 1] = nums1[m - 1]
        m -= 1
    else:
        nums1[m + n - 1] = nums2[n - 1]
        n -= 1
if n > 0:
    nums1[m + n - 1] = nums2[n - 1]