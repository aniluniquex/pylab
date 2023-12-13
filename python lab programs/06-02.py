# to print the sum of corner elemebts in matrix
def sum_corners(matrix):
    r = len(matrix)
    c = len(matrix[0])
    return matrix[0][0] + matrix[0][c-1] + matrix[r-1][0] + matrix[r-1][c-1]

r = int(input("emter no of rows:"))
c = int(input("emter no of cols:"))

matrix = []

for i in range(r):
    r = []
    for j in range(c):
        element = int(input(f"enter element at {i} and {j} position: "))
        r.append(element)
    matrix.append(r)


print(f"The matrix you entered is {matrix} and sum is {sum_corners(matrix)}")