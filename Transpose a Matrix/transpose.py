# -------------------------------
# Type - 1 (Transpose using nested loops)
# -------------------------------

# Define matrix A
A = [
    [1, 5, 8],
    [4, 6, 7],
    [7, 2, 3]
]

# Transpose the matrix (in-place modification)
for i in range(len(A)):
    for j in range(len(A)):
        if i < j:   # Swap elements only above diagonal
            A[i][j], A[j][i] = A[j][i], A[i][j]

# Print transposed matrix
print("Transpose of matrix is:")
for r in A:
    print(r)

# -------------------------------
# Type - 2 (Transpose using list comprehension)
# -------------------------------

# Using list comprehension to create transposed matrix
transpose_list = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

# Print transposed matrix
print("Transpose of matrix (using list comprehension):")
for r in transpose_list:
    print(r)

# -------------------------------
# Example Output:
# Original Matrix:
# [1, 5, 8]
# [4, 6, 7]
# [7, 2, 3]
#
# Transposed Matrix:
# [1, 4, 7]
# [5, 6, 2]
# [8, 7, 3]
# -------------------------------