from relax import *
a = Matrix(3, 1)
a.import_matrix_from_file()
if a.split_matrix('matrix').is_symmetric():
    print('Входная матрица симметрична. Можем продолжать.')
else:
    print('Матрица не симметрична. Выход из программы')
    sys.exit()
b = a.split_matrix('matrix')
c = a.split_matrix('answers')

if not b.sylvesters_criterion():
    print('Матрица не удовлетворяет критерию Сильвестра')
    b = Matrix.mult(b, b.transpose())
    c = Matrix.mult(b.transpose(), c)

print('Приводим матрицу к удобному виду...')


Matrix.comfortable_view(b, c)

#for i in range(0, len(b.matrix)):
#    b.matrix[i][i] = 0
cur_residual, prev_residual = Matrix(3, 1), Matrix(3, 1)
prev_residual.matrix = [[0], [0], [0]]
cur_residual.matrix = [[0], [0], [0]]
while Matrix.stop_condition(cur_residual, prev_residual):
    tmp = Matrix.vector_sum(cur_residual.negative(), Matrix.mult(b, cur_residual))
    rk = Matrix.vector_sum(c, tmp)
    for i in range(0,len(prev_residual.matrix)):
        for j in range(0, len(prev_residual.matrix[0])):
            prev_residual.matrix[i][j] = cur_residual.matrix[i][j]
    cur_residual.matrix[rk.max_index()][0] = cur_residual.matrix[rk.max_index()][0] + rk.matrix[rk.max_index()][0]
    print(cur_residual.matrix)
    print(prev_residual.matrix)
    print(rk.matrix)
