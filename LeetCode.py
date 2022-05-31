class ListNode:
    def __init__(self, val=0, nextNode=None):
        self.val = val
        self.next = nextNode

    def list_to_node(self, arr):
        if len(arr) < 1:
            return None
        if len(arr) == 1:
            self.val = arr[0]
            return ListNode(arr[0])
        l0 = temp = ListNode(arr[0])
        for i in range(1, len(arr)):
            temp.next = ListNode(arr[i])
            temp = temp.next
        return l0

    def del_node(self, node):  # Delete Node in a Linked List
        temp = self
        while temp.next is not None:
            if node.val == temp.next.val:
                temp.next = temp.next.next
                break
            temp = temp.next

    def print(self):
        temp = self
        while temp is not None:
            print(temp.val)
            temp = temp.next

    def len(self):
        i, temp = 0, self
        while temp is not None:
            i += 1
            temp = temp.next
        return i

    def removeNthFromEnd(self, n):
        temp = self
        for i in range(temp.len() - n - 1):
            temp = temp.next
        temp.next = temp.next.next

    def reverseList(self):
        temp = self
        result = None
        while temp is not None:
            t1 = temp.next
            temp.next = result
            result = temp
            temp = t1
        return result


# # Linked List Cycle
# # Floyd’s Cycle-Finding Algorithm
# def hasCycle(head=ListNode()):
#     slow_p = fast_p = head
#     while slow_p and fast_p and fast_p.next:
#         slow_p = slow_p.next
#         fast_p = fast_p.next.next
#         if slow_p == fast_p:
#             return True
#     return False
#
#
# head = ListNode().list_to_node([3,2,0,-4])
# head.next.next.next.next = head.next
# print(hasCycle(head))


# # Palindrome Linked List
# def isPalindrome(head=ListNode()):
#     def copy_to_arr(head=ListNode()):
#         arr = []
#         while head:
#             arr.append(head.val)
#             head = head.next
#         return arr
#
#     arr = copy_to_arr(head)
#     for i in range(len(arr) // 2):
#         if arr[i] != arr[-1 - i]:
#             return False
#     return True
#
#
# head = ListNode().list_to_node([1, 2, 2, 1])
# print(isPalindrome(head))

# # Merge Two Sorted Lists
# def mergeTwoLists(list1=ListNode(), list2=ListNode()):
#     if list1.val > list2.val:
#         result = list2
#         list2 = list2.next
#     else:
#         result = list1
#         list1 = list1.next
#     temp = result
#     while list1 and list2:
#         if list1.val > list2.val:
#             temp.next = list2
#             list2 = list2.next
#         else:
#             temp.next = list1
#             list1 = list1.next
#         temp = temp.next
#     if list1 is not None:
#         temp.next = list1
#     else:
#         temp.next = list2
#     return result
#
#
# list1 = ListNode().list_to_node([1, 2, 4])
# list2 = ListNode().list_to_node([1, 3, 4])
# list3 = mergeTwoLists(list1, list2)
# list3.print()

# # Reverse Linked List
# head = ListNode().list_to_node([1,2,3,4,5])
# r_head = head.reverseList()
# r_head.print()


# # Remove Nth Node From End of List
# head = ListNode().list_to_node([1, 2, 3, 4, 5])
# n = 2
# head.removeNthFromEnd(n)
# head.print()


# # Delete Node in a Linked List
# head = ListNode().list_to_node([4,5,1,9])
# node = ListNode().list_to_node([1])
# head.del_node(node)
# head.print()


# # String to Integer (atoi)
# def myAtoi(s):
#     i = 0
#     while s[i] == ' ':
#         i += 1
#     znak = 1
#     if s[i] == '-':
#         znak = -1
#         i +=1
#     elif s[i] == '+':
#         i += 1
#     int_s = ''
#     while i < len(s):
#         if '0' <= s[i] <= '9':
#             int_s += s[i]
#             i += 1
#         else:
#             break
#     int_s = int(int_s) * znak
#     if int_s > 2147483647:
#         int_s = 2147483647
#     if int_s < -2147483648:
#         int_s = -2147483648
#     return int_s
#
#
# s = "4193 with words"
# print(myAtoi(s))

# # Valid Palindrome
# def isPalindrome(s):
#     s = list(s.lower())
#     i = 0
#     while i < len(s):
#         if s[i].isalnum():
#             i += 1
#             continue
#         else:
#             s.pop(i)
#     if s == s[::-1]:
#         return True
#     else:
#         return False
#
#
# s = "race a car"
# print(isPalindrome(s))


# # Valid Anagram
# def is_anagram(s, t):
#     s,t = list(s), list(t)
#     s.sort()
#     t.sort()
#     if s == t:
#         return True
#     else:
#         return False
#
#
# s = "anagram"
# t = "nagaram"
# print(is_anagram(s, t))


# # First Unique Character in a String
# def first_uniq_char(s):
#     for i in range(len(s)):
#         if s.rfind(s[i]) == s.find(s[i]):
#             return i
#     return -1
#
#
# s = "loveleetcode"
# print(first_uniq_char(s))


# # Reverse Integer
# def reverse(x):
#     znak = 1
#     x = list(str(x))
#     x.reverse()
#     if x[-1] == '-':
#         x.pop()
#         znak = -1
#     x = int(''.join(x)) * znak
#     return x
#
#
# x = 120
# x = reverse(x)
# print(x)
#

# # Reverse String
# def reverseString(s):
#     s.reverse()
#
#
# s = ["h","e","l","l","o"]
# reverseString(s)
# print(s)


# # Rotate Image 2
# def rotate(matrix):
#     matrix.reverse()
#     for i in range(len(matrix)):
#         for j in range(i):
#             matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
#
#
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# print(matrix)
# rotate(matrix)
# print(matrix)


# # Rotate Image
# def rotate(matrix):
#     temp = list(list(temp) for temp in list(zip(*matrix[::-1])))
#     for i in range(len(temp)):
#         matrix[i] = temp [i]
#
#
# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# rotate(matrix)
# print(matrix)


# # Valid Sudoku
# def is_valid_sudoku(board):
#     # Валидатор строки или столбца
#     def is_valid_string(string):
#         for j in string:
#             if j == '.':
#                 continue
#             if string.count(j) > 1:
#                 return False
#         return True
#
#     # Вытянуть подмассив 3х3 из массива 9х9 в одномерный список
#     def mini_board(a1, a2, b1, b2, board):
#         string = []
#         for i in range(a1, a2):
#             for j in range(b1, b2):
#                 string.append(board[i][j])
#         return string
#
#     for i in board:
#         if is_valid_string(i):
#             continue
#         else:
#             return False
#
#     for i in range(9):
#         column = [line[i] for line in board]
#         if is_valid_string(column):
#             continue
#         else:
#             return False
#
#     for i in range(0, 9, 3):
#         for j in range(0, 9, 3):
#             mini_sudoku = mini_board(i, i + 3, j, j + 3, board)
#             if is_valid_string(mini_sudoku):
#                 continue
#             else:
#                 return False
#     return True
#
#
# board = [["8", "3", ".", ".", "7", ".", ".", ".", "."]
#     , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
#     , [".", "9", "8", ".", ".", ".", ".", "6", "."]
#     , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
#     , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
#     , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
#     , [".", "6", ".", ".", ".", ".", "2", "8", "."]
#     , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
#     , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
# print(is_valid_sudoku(board))

# # Two Sum
# def two_sum(nums, target):
#     for i in range(len(nums)-1):
#         b = target - nums[i]
#         try:
#             ii = nums.index(b, i + 1)
#         except ValueError:
#             continue
#         return [i, ii]
#     return 'таких пар нет'
#
#
# nums = [3,2,3]
# target = 6
# print(two_sum(nums, target))

# # Move Zeroes
# def move_zeroes(nums):
#     i = 0
#     nums_len = len(nums)
#     while i < nums_len:
#         if nums[i] == 0:
#             del(nums[i])
#             nums.append(0)
#             nums_len -= 1
#             continue
#         i += 1
#
#
# nums = [0,1,0,3,12]
# move_zeroes(nums)
# print(nums)


# def single_number(nums):
#     if len(nums) == 1:
#         return nums[0]
#     nums.sort()
#     for i in range(0, len(nums)-1, 2):
#         if nums[i] != nums[i+1]:
#             return nums[i]
#     return nums[-1]
#
#
# arr = [1]
# print(single_number(arr))


# # Contains Duplicate
# def contain_duplicate (nums):
#     nums.sort()
#     for i in range(len(nums)-1):
#         if nums[i] == nums[i+1]:
#             return True
#     return False
#
#
# arr = [1,2,3,4]
# print(contain_duplicate(arr))


# # Rotate Array
# def rotate(nums, k):
#     k = len(nums) - k
#     nums.extend(nums[:k])
#     del nums[:k]
#
#
# nums = [1,2,3,4,5,6,7]
# k = 3
# rotate(nums, k)
# print(nums)


# # Best Time to Buy and Sell Stock II
# class Solution:
#     def maxProfit(self, prices):
#         profit = 0
#         for i in range(len(prices) - 1):
#             profit_day = prices[i + 1] - prices[i]
#             if profit_day <= 0:
#                 continue
#             profit += profit_day
#         return profit


# Remove Duplicates from Sorted Array
# def remove_duplicates(nums):
#     for i in range((len(nums)-1)):
#         while
#
#
#         print (i)
#         if nums[i] == nums[i+1]:
#             print(nums[i])
#             nums.pop(i+1)
#             print(nums)
#             # i -= 1
#     return len(nums)
#
#
# nums = [11, 11, 2]
#
# remove_duplicates(nums)
# print(nums)


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
