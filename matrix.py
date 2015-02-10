import sys


class VectorError(Exception):
    def __init__(self, message):
        self.message = message


class Matrix:
# Конструктор
# params(i_count int, j_count int)
    def __init__(self, i_count, j_count):
        self.i = i_count
        self.j = j_count
        self.matrix = list()

# Метод для ввода матрицы с клавиатуры

    def create(self):
        print('Создаем новую матрицу {i_count}x{j_count} ...'.format(i_count=self.i, j_count=self.j))
        for a in range(0, self.i):
            row = []
            el = input('Введите через запятую элементы {row} строки: '.format(row=a+1)).split(',')
            if len(el) != self.j:
                print('Неверное количество элементов. Вы создавали матрицу с {j} столбацами'.format(j = self.j))
                break
            else:
                for it in el:
                    row.append(float(it))
                self.matrix.append(row)

# Метод для чтения матрицы из файла
# params (filename string (optional))

    def import_matrix_from_file(self, filename='matrix.txt'):
        try:
            f = open(filename)
            for line in f:
                row = []
                str_row = line.split(',')
                for el in str_row:
                    row.append(float(el))
                self.matrix.append(row)
        except FileNotFoundError:
            print('Неверное имя файла! Попробуйте еще раз.')
            self.import_matrix_from_file(input('Введите имя файла: '))
        except ValueError:
            print('В файле что то не является числом! Измените неккоректное значение в файле и повторите.')
            sys.exit()

# Метод проверяет матрицу на симметричность

    def is_symmetric(self):
        symmetric = True
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if self.matrix[i][j] != self.matrix[j][i]:
                    symmetric = False
        return symmetric

# Метод проверяет матрицу на критерий сильвестра

    def sylvesters_criterion(self):
        det2 = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        det3 = self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] - self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1] - self.matrix[0][1]*self.matrix[1][0]*self.matrix[2][2] + self.matrix[0][1]*self.matrix[1][2]*self.matrix[2][0] +self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1] - self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]
        if self.matrix[0][0] >= 0 and det2 >= 0 and det3 >= 0:
            return True
        else:
            return False

# Приводит матрицу к удобному для вычислений виду согласно алгоритму метода релаксации

    @staticmethod
    def comfortable_view(matrix, answers):
        new_matrix, new_answers = list(), list()
        current_main_elem = 0
        main_elems = []
        for row in matrix.matrix:
            new_row = []
            for el in row:
                new_row.append(el/row[current_main_elem] * -1)
            main_elems.append(row[current_main_elem])
            new_matrix.append(new_row)
            current_main_elem += 1

        for j in range(0, len(answers.matrix)):
            answers.matrix[j][0] = answers.matrix[j][0]/main_elems[j]
        matrix.matrix = new_matrix

# Отделяет матрицу с переменными или ответами от исходной (4х3) матрицы

    def split_matrix(self, what_should_i_split):
        if what_should_i_split == "matrix":
            new_obj = Matrix(self.i - 1, self.j - 1)
            split_param1 = 0
            split_param2 = len(self.matrix[0]) - 1
        else:
            new_obj = Matrix(3,1)
            split_param1 = len(self.matrix[0]) - 1
            split_param2 = split_param1 + 1
        new_matrix = []
        for row in self.matrix:
            new_row = row[split_param1: split_param2]
            new_matrix.append(new_row)
        new_obj.matrix = new_matrix
        return new_obj

# Метод умножения двух матриц

    @staticmethod
    def mult(m1, m2):
        global m3
        row_sum = 0
        row = []
        if len(m2.matrix) != len(m1.matrix[0]):
            print("Матрицы не могут быть перемножены")
        else:
            r1 = len(m1.matrix)
            c1 = len(m1.matrix[0])
            r2 = c1
            c2 = len(m2.matrix[0])
            m3 = Matrix(r1, c2)
            for z in range(0, r1):
                for j in range(0, c2):
                    for i in range(0, c1):
                       row_sum = row_sum+m1.matrix[z][i] * m2.matrix[i][j]
                       round(row_sum, 5)
                    row.append(row_sum)
                    row_sum = 0
                m3.matrix.append(row)
                row = []
        return m3

# Возвращает индекс максимального элемента в векторе

    def max_index(self):
        if self.j != 1:
            raise VectorError('В функцию нахождения индекса передан не вектор')
        index = 0
        array = list()
        for row in self.matrix:
            for el in row:
                array.append(el)
            while array[index] != max(array):
                index += 1
        return index

# Возвращает индекс максимального по модулю элемента в векторе

    def max_index_abs(self):
        if self.j != 1:
            raise VectorError('В функцию нахождения индекса передан не вектор')
            return
        index = 0
        array = list()
        for row in self.matrix:
            for el in row:
                array.append(abs(el))
            while array[index] != max(array):
                index += 1
        return index

# Суммирует
    @staticmethod
    def vector_sum(matrix1, matrix2):
        vector1 = []
        vector2 = []
        result = Matrix(3, 1)
        for row in matrix1.matrix:
            for element in row:
                vector1.append(element)
        for row in matrix2.matrix:
            for element in row:
                vector2.append(element)
        i = 0
        for el in vector1:
            new_row = list()
            new_row.append(round(el + vector2[i], 5))
            result.matrix.append(new_row)
            i += 1
        return result

# Транспонирует матрицу

    def transpose(self):
        new_matrix = Matrix(self.j, self.i)
        matrix = []
        new_row0, new_row1, new_row2 = [], [], []
        for row in self.matrix:
            new_row0.append(row[0])
            new_row1.append(row[1])
            new_row2.append(row[2])
        matrix.append(new_row0)
        matrix.append(new_row1) 
        matrix.append(new_row2)
        new_matrix.matrix = matrix
        return new_matrix

# Умножение на -1 (вектора)

    def negative(self):
        matrix = Matrix(3, 1)
        new_matrix = list()
        for row in self.matrix:
            new_row = list()
            for element in row:
                new_row.append(-element)
            new_matrix.append(new_row)
        matrix.matrix = new_matrix
        return matrix

# Нормирует вектор

    def to_norm(self):
        if self.j != 1:
            raise VectorError('В функцию нахождения индекса передан не вектор')
        max_index = self.max_index_abs()
        for row in self.matrix:
            row[0] = row[0] / abs(self.matrix[max_index][0])

# Скалярное произведение векторов

    @staticmethod
    def vector_scalar_mult(vec1, vec2):
        res = 0
        for i in range(0, len(vec1.matrix)):
            res += (vec1.matrix[i][0] * vec2.matrix[i][0])
        return res

# Распечатывает матрицу построчно

    def print(self):
        for i in range(0, len(self.matrix)):
            print('|' + str(self.matrix[i]) + '|\n')

# Нахождение первой лямбды

    @staticmethod
    def first_lambda(matrix, vec1, count):
        lam, lam1 = 1, 0
        arr = matrix.matrix
        while abs(lam1 - lam) > 0.000001:
            count += 1
            lam = lam1
            vec2 = Matrix.mult(matrix, vec1)  # Y(k+1) = AY(k)
            lam1 = Matrix.vector_scalar_mult(vec2, vec1) / Matrix.vector_scalar_mult(vec1, vec1)
            if count % 5 == 0:
                vec2.to_norm()
            vec1 = vec2  # Y(k) = y(k+1)
        return lam1

    @staticmethod
    def second_lambda(vec1, matrix, lamf, count):
        lam, lam1 = lamf, 0
        vec2 = Matrix(3, 1)
        vec2.matrix = [[1], [1], [1]]
        while abs(lam1 - lam) > 0.1:
            count += 1
            lam = lam1
            vec3 = Matrix.mult(matrix, vec2)
            lam1 = (Matrix.vector_scalar_mult(vec3, vec2) - lamf * Matrix.vector_scalar_mult(vec2, vec2)) / (Matrix.vector_scalar_mult(vec2, vec2) - lamf * Matrix.vector_scalar_mult(vec1, vec2))
            if count % 5 == 0:
                for i in range(0, len(vec2.matrix)):
                    vec2.matrix[i][0] = vec2.matrix[i][0] / vec3.max_index_abs()
            vec1 = vec2
            vec2 = vec3
        return lam1










