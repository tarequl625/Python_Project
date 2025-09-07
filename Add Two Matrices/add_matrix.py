# -------------------------------
# Type - 1 (Matrix Addition with predefined values)
# -------------------------------
A = [[1, 5, 8],
     [4, 6, 7],
     [7, 2, 3]]

B = [[4, 5, 6],
     [8, 9, 1],
     [3, 5, 6]]

# Result matrix initialized with zeros (same size as A and B)
result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Loop through rows
for i in range(len(A)):
    # Loop through columns
    for j in range(len(A[0])):
        # Add corresponding elements of A and B
        result[i][j] = A[i][j] + B[i][j]

# Display the result
for r in result:
    print(r)

# -------------------------------
# Example Output:
# [5, 10, 14]
# [12, 15, 8]
# [10, 7, 9]
# -------------------------------