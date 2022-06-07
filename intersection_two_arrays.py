nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

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

print(out)

