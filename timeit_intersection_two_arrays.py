setup = """
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
"""

double_while = """
out = []
i = len(nums1) - 1

while i >= 0:
    j = len(nums2) - 1
    if j < 0:
        break
    while j >= 0:
        if nums1[i] == nums2[j]:
            out.append(nums1[i])
            nums2.pop(j)
            break
        j -= 1
    i -= 1
"""

sort_and_two_pointers = """
nums1.sort()
nums2.sort()

ans = []
i = j = 0
while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        i += 1
    elif nums1[i] > nums2[j]:
        j += 1
    else:
        ans.append(nums1[i])
        i += 1
        j += 1
"""

import timeit
print(timeit.timeit(setup=setup, stmt=double_while, number=1000))
print(timeit.timeit(setup=setup, stmt=sort_and_two_pointers, number=1000))
