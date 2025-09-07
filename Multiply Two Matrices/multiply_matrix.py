# -------------------------------
# Matrix Multiplication (3x3 Matrices)
# -------------------------------

# Define first matrix A
A = [
    [1, 5, 8],
    [4, 6, 7],
    [7, 2, 3]
]

# Define second matrix B
B = [
    [4, 5, 6],
    [8, 9, 1],
    [3, 5, 6]
]

# Initialize result matrix with zeros
result = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Perform matrix multiplication
for i in range(len(A)):           # Loop through rows of A
    for j in range(len(B[0])):    # Loop through columns of B
        for k in range(len(B)):   # Loop through rows of B / columns of A
            result[i][j] += A[i][k] * B[k][j]

# Print the result matrix
print("Result of A x B is:")
for r in result:
    print(r)

# -------------------------------
# Example Output:
# Result of A x B is:
# [77, 98, 50]
# [86, 97, 73]
# [45, 64, 57]
# -------------------------------