Y = 20
X = 10
A = [ [0]*Y for i in range(X) ]

for i in range(X):
    for j in range(Y//2):
        if i == j:
            A[i][j]=1
            A[i][19-j]=1

for row in A:
    for elem in row:
        print(elem, end = '  ')
    print()

print('-9 -8 -7 -6 -5 -4 -3 -2 -1 0  1  2  3  4  5  6  7  8  9 10')