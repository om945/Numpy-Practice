import numpy as np

ages = np.array([[21, 34, 10, 14, 56, 99],
                 [34, 12, 76, 88, 23, 25]])

adults = np.where(ages >= 18, ages, 0)

print(adults)