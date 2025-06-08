A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
S = []
for i in range(len(A)):
    X = []
    for j in range(len(A[0])):
        X.append(A[i][j] + B[i][j])
    S.append(X)
print(S)


