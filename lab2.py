__author__ = 'nikitakochnev'

from matrix import *

a = Matrix(3, 3)
b = Matrix(3, 1)
a.import_matrix_from_file('matrix_lab2.txt')
b.matrix = [[1], [1], [1]]
count = 0
l = Matrix.first_lambda(a, b, count)
l2 = Matrix.second_lambda(b, a, l, count)
a.print()
print('1st Lambda: ' + str(l) + '\n\n' + '2nd lambda: ' + str(l2))


