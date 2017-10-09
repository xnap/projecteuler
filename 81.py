matrix = []
for line in open('p081_matrix.txt'):
    nums = line.rstrip().split(',')
    matrix.append(nums)

len = 80
res = [[0] * len] * len
for i in range(0, len):
    for j in range(0, len):
        if i == 0 and j == 0:
            res[0][0] = int(matrix[i][j])
        elif i == 0:
            res[0][j] = int(matrix[i][j]) + res[0][j-1]
        elif j == 0:
            res[i][0] = int(matrix[i][j]) + res[i-1][0]
        else:
            res[i][j] = int(matrix[i][j]) + min(res[i-1][j], res[i][j-1])
print(res[len-1][len-1])

