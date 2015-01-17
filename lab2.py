__author__ = 'nikitakochnev'

from matrix import *

a = Matrix(3, 1)

"""
Вводим матрицу из файла.
Если не передавать значений в метод, то по умолчанию считается что имя файла "matrix.txt"
"""

a.import_matrix_from_file('matrix_lab2.txt')
print(a.matrix)