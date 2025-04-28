from numpy.matrixlib.defmatrix import matrix

m1 = matrix('11 2 10; 1 5 1')
m2 = matrix('2 0 2; 0 9 1')

print(m1)
print(m2)

m3 = m1 + m2
print(m3)

m4 = m1 *2
print(m4)

m2 = [[2, 0, 2],
      [0, 9, 1]]

transpose_m2 = []

for i in range(len(m2[0])):
    row = []
    for j in range(len(m2)):
        row.append(m2[j][i])
    transpose_m2.append(row)

for m5 in transpose_m2:
    print(m5)

m3 = [
    [13, 2, 12],
    [1, 14, 2]
]

m5 = [
    [2, 0],
    [0, 9],
    [2, 1]
]
result = []

for i in range(len(m3)):
    row = []
    for j in range(len(m5[0])):
        sum = 0
        for k in range(len(m5)):
            sum += m3[i][k] * m5[k][j]
        row.append(sum)
    result.append(row)

for m6 in result:
    print(m6)

sum_of_elements = 0

for row in m3:
    for element in row:
        sum_of_elements += element

print(sum_of_elements)

m = [
    [0, 0, 0],
    [0, 0, 0]
]

for m7 in m:
    print(m7)
