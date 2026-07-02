import numpy as np

# aggregate function = summarize data and typically return a single value

arr = np.array([[1, 2, 3, 4, 5],
               [6, 7, 8, 9, 10]]) 

# print(np.sum(arr))
# print(np.mean(arr))
# print(np.std(arr)) # Standard deviation
# print(np.var(arr)) #Variance
# print(np.min(arr))
# print(np.max(arr))
# print(np.argmin(arr)) # Argument min
# print(np.argmax(arr)) # Argument max

print(np.sum(arr, axis=0))
print(np.sum(arr, axis=1))
