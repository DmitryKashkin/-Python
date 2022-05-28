# Longest Common Prefix
def longestCommonPrefix(strs):
    result = ''
    j = 0
    while j < len(strs[0]):
        i = 1
        while i < len(strs) and j < len(strs[i]):
            if strs[0][j] == strs[i][j]:
                i += 1
                continue
            else:
                return result
        result += strs[0][j]
        j += 1
    return result


strs = ["flower","flow","flight"]
strs = ["dog","racecar","car"]
print(longestCommonPrefix(strs))


# # Implement strStr()
# def strStr(haystack, needle):
#     if needle == '':
#         return 0
#     i = 0
#     while i + len(needle) <= len(haystack):
#         if needle == haystack[i:i+len(needle)]:
#             return i
#         i += 1
#     return -1
#
#
# haystack = "aaaaa"
# needle = "bba"
# print(strStr(haystack, needle))


# # Plus One
# def plus_one(digits):
#     result = int(''.join(str(n) for n in digits))
#     # print(result)
#     result += 1
#     return list(map(int, str(result)))
#
#
# digits = [9]
# print(plus_one(digits))



# # Intersection of Two Arrays II
# def intersect(nums1, nums2):
#     result = []
#     for i in nums1:
#         for j in nums2:
#             if i == j:
#                 result.append(i)
#                 nums2.remove(j)
#                 break
#     return result
#
#
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
# print(nums1, nums2, intersect(nums1, nums2))

# def removeDuplicates(nums):
#     i = 0
#     lenght = len(nums) - 1
#     while i < lenght:
#         if nums[i] == nums[i + 1]:
#             del nums[i]
#             lenght -= 1
#         else:
#             i += 1
#     return lenght + 1
#
#
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# print(nums)
# print(removeDuplicates(nums))
# print(nums)
