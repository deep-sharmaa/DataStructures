
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

key = 9

# indx = arr.index(key)

# print(indx)

# for i in range(0, len(arr)-1):
#     if arr[i] == key:
#         print("bro index is at: ", i)
#         break
#     else:
#         print("i am here")


#O(logN) solution using binary search, find the mid by separating low and high value and divide by 2 

key = 3

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]

l = 0
h = len(arr)-1


def search(arr, l, h, key):
    if l > h:
        return -1

    print("h is here")
 
    mid = (l + h) // 2

    if arr[mid] == key:
        print("i m coming in when mid is equal to key", mid)
        return mid
 
    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:
 
        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        print("i am going outside first condition")
        return search(arr, mid + 1, h, key)
 
    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search(arr, mid + 1, h, key)
    print("i am going outside second condition")
    return search(arr, l, mid-1, key)


search(arr, l, h, key)


