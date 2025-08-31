import numpy as np

#Sum together every number from 0 to 10000 except for those than can be divided by 4 or 7. Do this in one line of code

# --------------------------
# Step 1: np.arange(10001) → generates numbers 0,1,2,...,10000
# Step 2: (np.arange(10001)%4 != 0) → True for numbers not divisible by 4
# Step 3: (np.arange(10001)%7 != 0) → True for numbers not divisible by 7
# Step 4: Multiply the boolean arrays (*) → acts like logical AND in NumPy
# Step 5: np.arange(...)[mask] → selects numbers not divisible by 4 or 7
# Step 6: np.sum(...) → sums all the selected numbers

print(np.sum(np.arange(10001)[(np.arange(10001)%4!=0)*(np.arange(10001)%7!=0)]))

# --------------------------
# Example explorations
# --------------------------

# Generate array from 1 to 9 (step 1)
print(np.arange(1,10,1))  # Output: [1 2 3 4 5 6 7 8 9]

# Access the 3rd element (index 2)
print(np.arange(1,10,1)[2])  # Output: 3

# Boolean mask for numbers not divisible by 4 or 7
print((np.arange(1,10,1)%4!=0)*(np.arange(1,10,1)%7!=0))  
# Output: [ True  True False  True  True  True False  True  True]

# Filter the array using the mask
print(np.arange(1,10,1)[(np.arange(1,10,1)%4!=0)*(np.arange(1,10,1)%7!=0)])  
# Output: [1 2 4 5 6 8 9]

# Sum of the filtered array
print(np.arange(1,10,1)[(np.arange(1,10,1)%4!=0)*(np.arange(1,10,1)%7!=0)].sum())  
# Output: 35