# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions

# arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2

# Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
# Output: 5 6 7 1 2 3 4

a = [1, 2, 3, 4, 5, 6, 7]
d = 3

# c = a[2:]
# v = a[:2]


# c.extend(v)
# print(c)


i = 1

while i <= d:
    first_ele = a[0]
    a.remove(first_ele)
    a.append(first_ele)
    i += 1

print(a)
