from relax import *
a = Matrix(3, 1)
a.import_matrix_from_file()

c = a.split_matrix('matrix')
d = a.split_matrix('answers')

print(c.matrix)
print(d.matrix)
c.transpose()
print(c.matrix)