def remove_duplicates(nums):
    for i in range((len(nums)-1)):
        while


        print (i)
        if nums[i] == nums[i+1]:
            print(nums[i])
            nums.pop(i+1)
            print(nums)
            # i -= 1
    return len(nums)


nums = [11, 11, 2]

remove_duplicates(nums)
print(nums)



# Set Matrix Zeroes
# class Solution:
#     def setZeroes(self, matrix):
#         """
#         :type matrix: List[List[int]]
#         :rtype: void Do not return anything, modify matrix in-place instead.
#         """
#         R = len(matrix)
#         C = len(matrix[0])
#         rows, cols = set(), set()
#
#         # Essentially, we mark the rows and columns that are to be made zero
#         for i in range(R):
#             for j in range(C):
#                 if matrix[i][j] == 0:
#                     rows.add(i)
#                     cols.add(j)
#
#         # Iterate over the array once again and using the rows and cols sets, update the elements
#         for i in range(R):
#             for j in range(C):
#                 if i in rows or j in cols:
#                     matrix[i][j] = 0
#
#
# a = Solution
#
# m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# a.setZeroes(m, m)
# print(m)

