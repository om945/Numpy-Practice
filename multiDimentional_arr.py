import numpy as np

arr = np.array([[["A",'b', 'c'], ['D', 'E', 'F'],['G', 'H', 'I']],
                [["J",'K', 'K'], ['l', 'M', 'N'],['O', 'P', 'Q']],
                [["R",'S', 'T'], ['U', 'V', 'W'],['X', 'Y', ' ']],
                ])

print(arr.ndim)
print(arr.shape)
print(arr[0][0][0]) #chain indexing
print(arr[0, 0, 2])

word = arr[0, 0, 0] + arr[2,0,0]
print(word)