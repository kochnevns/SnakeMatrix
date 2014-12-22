from relax import *
a = Matrix(3, 1)
a.import_matrix_from_file()
if a.split_matrix('matrix').is_symmetric():
    print('Входная матрица симметрична. Можем продолжать.')
else:
    print('Матрица не симметрична. Выход из программы')
    sys.exit()
matrix = a.split_matrix('matrix')
answers = a.split_matrix('answers')



if not matrix.sylvesters_criterion():
    print('Матрица не удовлетворяет критерию Сильвестра')
    new_matrix = Matrix.mult(matrix, matrix.transpose())
    new_answers = Matrix.mult(matrix.transpose(), answers)
else:
    sys.exit()


print('Приводим матрицу к удобному виду...')

Matrix.comfortable_view(new_matrix, new_answers)


for i in range(0, len(new_matrix.matrix)):
    new_matrix.matrix[i][i] = 0


print(new_matrix.matrix)
print(new_answers.matrix)
numb_of_iter = 0
cur_aprox = Matrix(3,1)
for a in new_answers.matrix:
    row = list()
    row.append(a[0])
    cur_aprox.matrix.append(row)
prev_aprox = Matrix(3, 1)
prev_aprox.matrix = [[0], [0], [0]]

while Matrix.stop_condition(cur_aprox, prev_aprox, numb_of_iter):
    tmp = Matrix.vector_sum(cur_aprox.negative(), Matrix.mult(new_matrix, cur_aprox))
    rk = Matrix.vector_sum(tmp, new_answers)
    for i in range(0, len(cur_aprox.matrix) - 1):
        prev_aprox.matrix[i][0] = cur_aprox.matrix[i][0]
    cur_aprox.matrix[rk.max_index_abs()][0] = cur_aprox.matrix[rk.max_index_abs()][0] + rk.matrix[rk.max_index_abs()][0]
    numb_of_iter += 1


    print('Итерация # {numb}'.format(numb = numb_of_iter))
    print('Текущая невязка: ' + str(cur_aprox.matrix))
    print('Предыдущая невязка: ' + str(prev_aprox.matrix))
    print('----------------------------'* 3)



