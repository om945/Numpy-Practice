import numpy as np

arr = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])

# array[start:end:step]

print(arr[0:4:2])

# array[row, column]
print(arr[:, 0])
print(arr[:, 0:2])
print(arr[0:2, 0:2])

