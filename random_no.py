import numpy as np

rng = np.random.default_rng()

# print(rng.integers(low=1, high=7, size= 7))
# print(rng.integers(low=1, high=7, size= (3,2)))
# print(np.random.uniform(low=-1, high=1, size=3))

# rng = np.random.default_rng()
# arr = np.array([1,2,3,4,5])
# rng.shuffle(arr)
# print(arr)

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
fruits = rng.choice(fruits)
# fruits = rng.choice(fruits, size=3)
# fruits = rng.choice(fruits, size=(3,3))


print(fruits)