def findIntersectionValues(nums1, nums2):
    s1=0
    s2=0
    for i in range(len(nums1)):
        if nums1[i] in nums2:
            s1+=1
    for i in range(len(nums2)):
        if nums2[i] in nums1:
            s2+=1
    return [s1, s2]
nums1 = [4, 3, 2, 3, 1]
nums2 = [2, 2, 5, 2, 3, 6]
print(findIntersectionValues(nums1, nums2))
