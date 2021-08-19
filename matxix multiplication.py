X = [[1, 7, 3],
             [3, 5, 6],
             [6, 8, 9]]
Y = [[1, 1, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]]
 
# iterating by row of A
for i in range(len(X)):
 
    # iterating by column by B
    for j in range(len(Y[0])):
 
        # iterating by rows of B
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
 
for r in result:
    print(r)