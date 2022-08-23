# Find maximum value of Sum( i*arr[i]) with only rotations on given array allowed

# Given an array arr[] of size N, the task is to find the maximum possible sum of i*arr[i] when the array
# can be rotated any number of times.

# Input: arr[] = {1, 20, 2, 10}
# Output: 72. We can get 72 by rotating array twice.
# {2, 10, 1, 20}
# 20*3 + 1*2 + 10*1 + 2*0 = 72
#
# Input: arr[] = {10, 1, 2, 3, 4, 5, 6, 7, 8, 9}
# Output: 330
# We can get 330 by rotating array 9 times.
# {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
# 0*1 + 1*2 + 2*3 … 9*10 = 330


def maxSum(arr):
    # stores sum of arr[i]
    arrSum = 0

    print('arrSum:', arrSum)

    # stores sum of i*arr[i]
    currVal = 0

    print('currVal:', currVal)

    n = len(arr)

    print("length: ", n)

    for i in range(0, n):
        arrSum = arrSum + arr[i] # 21
        print('arrSum in  loop', arrSum)
        currVal = currVal + (i * arr[i]) # 20

        print('currVal in  loop', currVal)

    # initialize result
    maxVal = currVal

    print('maxVal in  loop', maxVal)

    # try all rotations one by one and find the maximum
    # rotation sum
    for j in range(1, n):
        currVal = currVal + arrSum - n * arr[n - j]
        if currVal > maxVal:
            maxVal = currVal

    print(maxVal)

    # return result
    return maxVal


# test maxsum(arr) function
if __name__ == '__main__':
    arr = [1, 20, 2, 10] #(1* 0 + 20* 1+ 2* 2 + 10*3 ) 20+4+30
    print("Max sum is: ", maxSum(arr))