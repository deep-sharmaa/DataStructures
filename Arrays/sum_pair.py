# Find if there is a pair with a given sum in the rotated sorted Array

# Given an array arr[] of distinct elements size N that is sorted and then around an unknown point, the task is to check if the array has a pair with a given sum X.

# Input: arr[] = {11, 15, 6, 8, 9, 10}, X = 16
# Output: true
# Explanation: There is a pair (6, 10) with sum 16

import enum

arr = [11, 15, 6, 8, 9, 10]
x = 21

# my solution 1

# for i in arr:
#     rem = x - i
#     if rem in arr and rem != i:
#         print(i, rem)
#         break

# my solution 2 (The time complexity of the below solution is O(n2) and doesn’t require any extra space, where n is the size of the input.)

# for i in range(len(arr) -1 ):
#     for j in range(i+1, len(arr)):
#         if arr[i] + arr[j] == x:
#             print(arr[i], arr[j])


# solution 3 (The time complexity of the above solution is O(n) and requires O(n) extra space, where n is the size of the input.)

myDict = {} # {11:1, 5:2, }

for i, e in enumerate(arr):

    key = x - e # 11

    if key in myDict:
        print(key, e )

    myDict[e] = i



            