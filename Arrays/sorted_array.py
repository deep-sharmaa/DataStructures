
# Search an element in a sorted and rotated Array

# Given a sorted and rotated array arr[] of size N and a key, the task is to find the key in the array.

# Note: Find the element in O(logN) time and assume that all the elements are distinct.

# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 3
# Output : Found at index 8

# Input  : arr[] = {5, 6, 7, 8, 9, 10, 1, 2, 3}, key = 30
# Output : Not found

# Input : arr[] = {30, 40, 50, 10, 20}, key = 10   
# Output : Found at index 3

#first solution

arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]

key = 30

indx = arr.index(key)

print(indx)

for i in range(0, len(arr)-1):
    if arr[i] == key:
        print("bro index is at: ", i)
        break
