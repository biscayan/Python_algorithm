# solution 1. two pointers
# runtime : 40 ms
# memory : 14.4 MB
def intersection(nums1, nums2):

    nums1.sort()
    nums2.sort()

    i, j = 0, 0
    num_set = set()

    while i < len(nums1) and j < len(nums2):
        if nums1[i] > nums2[j]:
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] == nums2[j]:
            num_set.add(nums1[i])
            i += 1
            j += 1

    return list(num_set)

# solution 2. set intersection
# runtime : 44 ms
# memory : 14.6 MB
def intersection(nums1, nums2):
    set1, set2 = set(nums1), set(nums2)
    num_set = set1 & set2
    return list(num_set)