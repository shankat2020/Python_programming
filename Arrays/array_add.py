"""Given an integer whose unique digits are values in an array
(123 would be [1, 2, 3]), write an algorithm that adds
one to the integer and returns the updated array.  """

def add_one(arr):



    n = len(arr)
    number = 0

    for i in range(0,n):
        number += arr[i]*(10**(n-i-1))
    print(number)

    number = number + 1
    new_arr = list(map(int, str(number)))


    print(new_arr)



add_one(arr = [1,2,3])
