# how to declare a matrix
mat = [[1,2,3], [4,5,6], [7,8,9]]
print(mat)

mat[0][1] = 10
print(mat)

# how to print a martix value using nested loop

for row in mat:
    for col in row:
        print(col)