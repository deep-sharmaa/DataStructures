# Given an array of integers arr[] of size N and an integer, the task is to rotate the array elements to the left by d positions

# arr[] = {1, 2, 3, 4, 5, 6, 7}, d = 2
# Output: 3 4 5 6 7 1 2

# Input: arr[] = {3, 4, 5, 6, 7, 1, 2}, d=2
# Output: 5 6 7 1 2 3 4

a = [1, 2, 3, 4, 5, 6, 7]
d = 2

#first solution

# c = a[d:] + a[:d]

# print(c)


# second solution

# i = 1

# while i <= d:
#     first_ele = a[0]
#     a.remove(first_ele)
#     a.append(first_ele)
#     i += 1

# print(a)



# Program to cyclically rotate an array by one [Imp one]

# Given an array, cyclically rotate the array clockwise by one. 

# Input:  arr[] = {1, 2, 3, 4, 5}
# Output: arr[] = {5, 1, 2, 3, 4}

cc = [1, 2, 3, 4, 5]
d = len(cc)

x = cc[d - 1]
     
for i in range(d - 1, 0, -1):
    cc[i] = cc[i - 1];
         
cc[0] = x;

# print(cc)


#another solution by using slicing

array = [1, 2, 3, 4, 5]
d = len(array)

print(array[-1:])
print(array[:-1])

array[:] = array[-1:]+array[:-1]

print(array)





