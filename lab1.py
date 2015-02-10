from matrix import *

a = Matrix(3, 1)

"""
Вводим матрицу из файла.
Если не передавать значений в метод, то по умолчанию считается что имя файла "matrix.txt"
"""

a.import_matrix_from_file()

if a.split_matrix('matrix').is_symmetric():
    print('Входная матрица симметрична. Можем продолжать.')
else:
    print('Матрица не симметрична. Выход из программы')
    sys.exit()
matrix = a.split_matrix('matrix')
answers = a.split_matrix('answers')
"""
Проверяем на критерий Сильвестра
Если не удовлетворяет - умножаем на транспонированную матрицу с коэфицентами перемменных обе матрицы
"""

if not matrix.sylvesters_criterion():
    print('Матрица не удовлетворяет критерию Сильвестра')
    new_matrix = Matrix.mult(matrix, matrix.transpose())
    new_answers = Matrix.mult(matrix.transpose(), answers)
else:
    sys.exit()

"""
Приводим матрицу к удобному для вычислений виду
"""

Matrix.comfortable_view(new_matrix, new_answers)
for i in range(0, len(new_matrix.matrix)):
    new_matrix.matrix[i][i] = 0

numb_of_iter = 0
cur_aprox = Matrix(3,1)
for a in new_answers.matrix:
    row = list()
    row.append(a[0])
    cur_aprox.matrix.append(row)
prev_aprox = Matrix(3, 1)
prev_aprox.matrix = [[0], [0], [0]]


for i in range(0, 1000):
    tmp = Matrix.vector_sum(cur_aprox.negative(), Matrix.mult(new_matrix, cur_aprox))
    rk = Matrix.vector_sum(tmp, new_answers)
    for i in range(0, len(cur_aprox.matrix)):
        prev_aprox.matrix[i][0] = cur_aprox.matrix[i][0]
    cur_aprox.matrix[rk.max_index_abs()][0] += rk.matrix[rk.max_index_abs()][0]
    numb_of_iter += 1
    print('Итерация # {numb}'.format(numb = numb_of_iter))
    print('Текущее приближение:    ' + str(cur_aprox.matrix))
    print('Предыдущее приближение: ' + str(prev_aprox.matrix))
    print('----------------------' * 4)
    tmp_vector = Matrix(3,1)
    tmp_matrix = []
    for i in range(0, len(cur_aprox.matrix)):
        tmp_row = list()
        tmp_row.append(cur_aprox.matrix[i][0] - prev_aprox.matrix[i][0])
        tmp_matrix.append(tmp_row)
    tmp_vector.matrix = tmp_matrix
    try:
        if abs(tmp_vector.matrix[Matrix.max_index_abs(tmp_vector)][0] / prev_aprox.matrix[Matrix.max_index_abs(prev_aprox)][0]) < 0.00001:
            print("Ответ: " + str(cur_aprox.matrix))
            print(rk.matrix)
            sys.exit()

    except ZeroDivisionError:
        continue



