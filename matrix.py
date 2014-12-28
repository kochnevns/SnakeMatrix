import sys


class Matrix:
### Конструктор
    def __init__(self, i_count, j_count):
        self.i = i_count
        self.j = j_count
        self.matrix = list()
### Вводим матрицу с клавиатуры

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

### Читаем и создаем матрицу из файла

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
### Проеряет на симметричность

    def is_symmetric(self):
        symmetric = True
        for i in range(0, len(self.matrix)):
            for j in range(0, len(self.matrix[i])):
                if self.matrix[i][j] != self.matrix[j][i]:
                    symmetric = False
        return symmetric

### Проверка на критерий сильвестра

    def sylvesters_criterion(self):
        det2 = self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        det3 = self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2] - self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1] - self.matrix[0][1]*self.matrix[1][0]*self.matrix[2][2] + self.matrix[0][1]*self.matrix[1][2]*self.matrix[2][0] +self.matrix[0][2] * self.matrix[1][0] * self.matrix[2][1] - self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]
        if self.matrix[0][0] >= 0 and det2 >= 0 and det3 >= 0:
            return True
        else:
            return False

### Приводит к удобному для вычислений виду
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

### Отделяет матрицу с переменными или ответами

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




### метод умножения двух матриц

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
            m3 = Matrix(c1, r2)
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

### индекс максимального элемента в векторе

    def max_index(self):
        index = 0
        array = list()
        for row in self.matrix:
            for el in row:
                array.append(el)
            while array[index] != max(array):
                index += 1
        return index

    def max_index_abs(self):
        index = 0
        array = list()
        for row in self.matrix:
            for el in row:
                array.append(abs(el))
            while array[index] != max(array):
                index += 1
        return index

    #сумма матриц
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

### транспонировать матрицу

    def transpose(self):
        new_matrix = Matrix(self.j, self.i)
        matrix = []
        i = 0
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

### умножение на -1

    def negative(self):
        matrix = Matrix(3,1)
        new_matrix = list()
        for row in self.matrix:
            new_row = list()
            for element in row:
                new_row.append(-element)
            new_matrix.append(new_row)
        matrix.matrix = new_matrix
        return matrix
    








