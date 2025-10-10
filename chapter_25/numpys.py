import numpy as np


my_array = np.array([1, 2, 3])
print(
    f"my_array: {my_array} | rank: {my_array.ndim} | size: {my_array.size} | shape: {my_array.shape}"
)

ranged_array = np.arange(10)
print(f"ranged_array: {ranged_array} | shape: {ranged_array.shape}")

zeros_array = np.zeros((3,))
print(f"zeros_array: {zeros_array} | shape: {zeros_array.shape}")

test_array = np.arange(10)
print(test_array)

reshaped_array = np.reshape(test_array, (5, 2))
print(reshaped_array)
print(reshaped_array[1, 1])

calculated_array = test_array * 2
print(calculated_array)
