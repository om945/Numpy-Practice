import numpy as np

## Scaler arithmetic

# arr = np.array([1.33, 2.5, 3.99])


# print(arr + 1)
# print(arr - 2)
# print(arr * 3)
# print(arr / 4)
# print(arr ** 5)

## Vectorized math function
# print(np.sqrt(arr))
# print(np.round(arr))
# print(np.floor(arr))
# print(np.ceil(arr))

# print(np.pi)

# radii = np.array([1, 2, 3])

# print(np.pi * radii ** 2)


# arr1 = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])

# print(arr1 + arr2)

## comparison operators

scores = np.array([91, 55, 100, 78, 82, 65])

print(scores == 100)
print(scores >= 60)
print(scores <= 60)

scores[scores < 60] = 0
print(scores )

