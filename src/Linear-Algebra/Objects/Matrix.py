'''A rectangular array of quantities or expressions in rows and columns that is treated as a single entity and manipulated according to particular rules.'''
'''
Representation: List of Lists
Properties: rows, cols, A
Methods: 
    row Swap - Elementary Row Operation
    row Multiply - Elementary Row operation
    row Sum - Elementary Row operation
    transpose - Returns a Matrix that is has the rows switched with the columns
    gaussian elimination - Solves a System of Linear Equations
    identity - Generates an identity matrix given rows
    concat - Concatenates 2 matrices together where the first is on the left and the new is on the right
    +, -, *, /, @ , where '@' is the Matrix Multiplication operator
    to string
'''


class Matrix:

    '''Matrix is initialized with a 2-dimensional array as input'''

    def __init__(self, array=[], rows=0, cols=0):
        # The Default Matrix is the identity Matrix if the matrix only has rows and cols defined
        if rows != 0 and cols != 0:
            self.rows = rows
            self.cols = cols
            self.A = [[1 if i == j else 0 for j in range(self.cols)] for i in range(self.rows)]
        # Otherwise, have a fully customizable Matrix Object if an array is given
        else:
            self.rows = len(array)
            self.cols = len(array[0])
            self.A = array

    '''Row Swap elementary row operation, Swap any two rows'''

    def swap(self, row1, row2):
        self.A[row1], self.A[row2] = self.A[row2], self.A[row1]
        return self

    '''Scalar Multiplication elementary row operation, Multiply any row by a constant'''

    def row_multiply(self, row1, scalar):
        temp = Matrix([self.A[row1]])*scalar
        self.A[row1] = temp.A[0]
        return self

    '''Row Sum elementary row operation, Add a multiple of one row to another row'''
    '''Will add Row1 to Row2, and the result will be stored in Row2'''

    def row_sum(self, row1, row2, multiple1=1, multiple2=1):
        mul1 = multiple1*Matrix([self.A[row1]])
        mul2 = multiple2*Matrix([self.A[row2]])
        temp = mul1+mul2
        self.A[row2] = temp.A[0]
        return self

    '''Matrix Transpose, switch Rows with Columns'''
    '''Input: This Matrix'''
    '''Output: Transpose Matrix'''

    def transpose(self):
        return Matrix([[row[i] for row in self.A] for i in range(self.rows)])

    '''Guassian Elimination, solves System of Linear Equations'''
    '''Input: This Matrix'''
    '''Output: Reduced Row Echelon Form Matrix'''

    def gauss_elimination(self):
        # 1. Swap the rows so that all the rows with all 0 entries are on the bottom
        last_zero = self.rows - 1
        # Create 0 row to compare other rows to
        zero_test = [0 for i in range(self.cols)]
        for row in range(self.rows - 1, 0, -1):
            if self.A[row] == zero_test and (last_zero < self.rows - 1):
                self.swap(row, last_zero)
                last_zero -= 1
            elif self.A[row] == zero_test and (last_zero >= self.rows - 1):
                last_zero -= 1

        # 5. Repeat steps 2-4 for the next leftmost nonzero entry until all the leading entries are 1.
        # Go from x0 to xn, but do not include b, which is the last column ; Note Pivot_row == Pivot_column
        for pivot_row in range(self.cols-1):

            # 2. Swap the rows so that the row with the largest, leftmost nonzero entry is on top.
            nth_column = [self.A[i][pivot_row] for i in range(
                last_zero)]  # Put pivot_column in place of 0
            self.swap(nth_column.index(max(nth_column)), 0)

            # 3. Multiply the top row by a scalar so that top row's leading entry becomes 1.
            # Put pivot_row in place of 0, [pivot_row][pivot_row]
            self.row_multiply(pivot_row, 1/self.A[pivot_row][pivot_row])

            # 4. Add/subtract multiples of the top row to the other rows so that all other entries in the column containing the top row's leading entry are all zero.
            for row in list(range(pivot_row)) + list(range(pivot_row+1, last_zero+1)):
                # Put pivot_column in place of 0, -row[0] ; Note: multiple1 will be equal to -rows_to_eliminate[row][pivot_column] because the number at pivot is always 1
                self.row_sum(pivot_row, row, multiple1=-self.A[row][pivot_row])

        # 6. Swap the rows so that the leading entry of each nonzero row is to the right of the leading entry of the row above it.
        # Go from x0 to xn, but do not include b, which is the last column
        for column in range(self.cols-1):
            temp = [self.A[i][column] for i in range(last_zero+1)]
            self.swap(temp.index(1), column)

        return self

    '''Identity, generates identity matrix size row'''

    def identity(self):
        for row in range(self.rows):
            for col in range(self.rows):
                if row == col:
                    self.A[row][col] = 1
                else:
                    self.A[row][col] = 0
        return self

    '''Concat, glues 2 matrices together left to right'''

    def Concat(self, other):
        bigger_rows = self.rows if self.rows > other.rows else other.rows
        smaller_rows = self.rows if self.rows < other.rows else other.rows
        who_is_smaller = self if self.rows < other.rows else other
        # if one of the matrices is too small, pad it with zeros until they are the same size in terms of the rows
        if bigger_rows > smaller_rows:
            difference = bigger_rows - smaller_rows
            # Should make difference amount of 0s rows to pad whoever is smaller
            who_is_smaller.A += ([[0 for i in range(who_is_smaller.cols)]]*difference)
            who_is_smaller.rows = who_is_smaller.rows + difference
        # loop through the bigger matrix's rows, or either if they are the same size in terms of rows
        for row in range(bigger_rows):
            # on each iteration, self.A[row] = self.A[row] + other.A[row]
            self.A[row] = self.A[row] + other.A[row]
        return self

    '''Overload Addition operator to define Addition operation for Matrix Objects'''
    '''Input: Matrix , Matrix or Matrix , Scalar'''
    '''Output: Matrix'''

    def __add__(self, other):
        # Create 0 matrix that is the size of the input matrix
        C = [[0 for j in range(self.cols)] for i in range(self.rows)]

        # Ensure other object is a Matrix
        if isinstance(other, Matrix):
            # Add each element of the Matrices together
            for i in range(self.rows):
                for j in range(self.cols):
                    C[i][j] = self.A[i][j] + other.A[i][j]

        elif isinstance(other, (int, float)):
            # Add the Matrix with the scalar
            for i in range(self.rows):
                for j in range(self.cols):
                    C[i][j] = self.A[i][j] + other

        # Note if other is neither a Matrix or a Scalar, this will return the 0 Matrix the size of the input Matrix
        return Matrix(C)

    '''Overload Left Addition operator to define Addition operation for Matrix Objects'''
    '''Input: Matrix , Matrix or Matrix , Scalar'''
    '''Output: Matrix'''

    def __radd__(self, other):
        return self.__add__(other)

    '''Overload Subtraction operator to define Subtraction operation for Matrix Objects'''
    '''Input: Matrix , Matrix or Matrix , Scalar'''
    '''Output: Matrix'''

    def __sub__(self, other):
        # Create 0 matrix that is the size of the input matrix
        C = [[0 for j in range(self.cols)] for i in range(self.rows)]

        # Ensure other object is a Matrix
        if isinstance(other, Matrix):
            # Subtract each element of the Matrices together
            for i in range(self.rows):
                for j in range(self.cols):
                    C[i][j] = self.A[i][j] - other.A[i][j]

        elif isinstance(other, (int, float)):
            # Subtract the Matrix with the scalar
            for i in range(self.rows):
                for j in range(self.cols):
                    C[i][j] = self.A[i][j] - other

        # Note if other is neither a Matrix or a Scalar, this will return the 0 Matrix the size of the input Matrix
        return Matrix(C)

    '''Overload Left Subtraction operator to define Subtraction operation for Matrix Objects'''
    '''Input: Matrix , Matrix or Matrix , Scalar'''
    '''Output: Matrix'''

    def __rsub__(self, other):
        return self.__sub__(other)

    '''Overload Multiplication operator to define Multiplication operation for Matrix Objects'''
    '''Input: Matrix , Scalar or Scalar , Matrix'''
    '''Output: Matrix'''

    def __mul__(self, other):

        C = [[0 for j in range(self.cols)] for i in range(self.rows)]

        if isinstance(other, Matrix):

            for i in range(self.rows):
                for j in range(self.cols):
                    C[i][j] = self.A[i][j] * other.A[i][j]

        # Scaler multiplication
        elif isinstance(other, (int, float)):

            for i in range(self.rows):
                for j in range(self.cols):
                    C[i][j] = self.A[i][j] * other

        return Matrix(C)

    '''Overload Left Multiplication operator to define Multiplication operation for Matrix Objects'''
    '''Input: Matrix , Scalar or Scalar , Matrix'''
    '''Output: Matrix'''

    def __rmul__(self, other):
        return self.__mul__(other)

    '''Overload Division operator to define Division operation for Matrix Objects'''
    '''Input: Matrix , Scalar or Scalar , Matrix'''
    '''Output: Matrix'''

    def __truediv__(self, other):

        C = [[0 for j in range(self.cols)] for i in range(self.rows)]

        if isinstance(other, Matrix):

            for i in range(self.rows):
                for j in range(self.cols):
                    C[i][j] = self.A[i][j] / other.A[i][j]

        # Scaler multiplication
        elif isinstance(other, (int, float)):

            for i in range(self.rows):
                for j in range(self.cols):
                    C[i][j] = self.A[i][j] / other

        return Matrix(C)

    '''Overload Left Division operator to define Division operation for Matrix Objects'''
    '''Input: Matrix , Scalar or Scalar , Matrix'''
    '''Output: Matrix'''

    def __rtruediv__(self, other):
        return self.__div__(other)

    '''Overload Matrix Multiplication operator to define Multiplication operation between Matrix, Matrix'''
    '''Input: Matrix , Matrix'''
    '''Output: Matrix'''

    def __matmul__(self, other):
        if isinstance(other, Matrix):
            C = [[0 for j in range(self.cols)] for i in range(self.rows)]

            # Multiply the elements in the same row of the first matrix
            # to the elements in the same col of the second matrix
            for i in range(self.rows):
                for j in range(self.cols):
                    acc = 0

                    for k in range(self.rows):
                        acc += self.A[i][k] * other.A[k][j]

                    C[i][j] = acc

        return Matrix(C)

    '''Get the item at the specified coordinates in a Matrix object'''

    def __getitem__(self, key):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            return self.A[i][j]

    '''Set the item at the specified coordinates in a Matrix object'''

    def __setitem__(self, key, value):
        if isinstance(key, tuple):
            i = key[0]
            j = key[1]
            self.A[i][j] = value

    '''Display the Matrix in the console'''

    def __str__(self):
        matrixString = ''
        for i in range(self.rows):
            matrixString += "  ".join(
                map(lambda x: '{0:8.3f}'.format(x), self.A[i]))+'\n'
        return matrixString


test = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
test2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
test3 = Matrix([[3, 2, -1, 1], [2, -2, 4, -2], [-1, .5, -1, 0]])
test4 = Matrix([[3, 2, -1, 1], [2, -2, 4, -2], [-1, .5, -1, 0]])
test5 = Matrix(rows=4, cols=4).Concat(Matrix(rows=2, cols=2))

'''
print("")
print("Test 1")
print("test+test2")
print("")
print("Expected:")
print("  10.000  10.000  10.000\n  10.000  10.000  10.000\n  10.000  10.000  10.000")
print("Got:")
print(test+test2)

print("")
print("Test 2")
print("test@test2")
print("")
print("Expected:")
print("  30.000  24.000  18.000\n  84.000  69.000  54.000\n  138.000  114.000  90.000")
print("Got:")
print(test@test2)

print("")
print("Test 3")
print("test*2")
print("")
print("Expected:")
print("  2.000  4.000  6.000\n  8.000  10.000  12.000\n  14.000  16.000  18.000")
print("Got:")
print(test*2)

print("")
print("Test 4")
print("test2-test")
print("")
print("Expected:")
print("  8.000  6.000  4.000\n  2.000  0.000  -2.000\n  -4.000  -6.000  -8.000")
print("Got:")
print(test2-test)

print("")
print("Test 5")
print("test/2")
print("")
print("Expected:")
print("  0.500  1.000  1.500\n  2.000  2.500  3.000\n  3.500  4.000  4.500")
print("Got:")
print(test/2)

print("")
print("Test 6")
print("test[0,1]")
print("")
print("Expected:")
print("2")
print("Got:")
print(test[0,1])

print("")
print("Test 7")
print("test[0,1] = 30000")
print("")
print("Expected:")
print("  1.000  30000.000  3.000\n  4.000  5.000  6.000\n  7.000  8.000  9.000")
print("Got:")
test[0,1] = 30000
print(test)
test[0,1] = 2

print("")
print("Test 8")
print("test.transpose()")
print("")
print("Expected:")
print("  1.000  4.000  7.000\n  2.000  5.000  8.000\n  3.000  6.000  9.000")
print("Got:")
print(test.transpose())

print("")
print("Test 9")
print("test.swap(1,2)")
print("")
print("Expected:")
print("  1.000  2.000  3.000\n  7.000  8.000  9.000\n  4.000  5.000  6.000")
print("Got:")
print(test.swap(1,2))
test.swap(1,2)

print("")
print("Test 10")
print("test.row_multiply(2,2)")
print("")
print("Expected:")
print("  1.000  2.000  3.000\n  4.000  5.000  6.000\n  14.000  16.000  18.000")
print("Got:")
print(test.row_multiply(2,2))
test.row_multiply(2,.5)

print("")
print("Test 11")
print("test.row_sum(1,2)")
print("")
print("Expected:")
print("  1.000  2.000  3.000\n  4.000  5.000  6.000\n  11.000  13.000  15.000")
print("Got:")
print(test.row_sum(1,2))

print("")
print("Test 12")
print("test4.gauss_elimination()")
print("")
print("Expected:")
#print("  1.000  0.000 0.000 1.000\n  0.000  1.000  0.000 -2.000\n  0.000  0.000  1.000 -2.000")
print("some stuff on the white board")
print("Got:")
print(test4.gauss_elimination())

'''
print("Test 13")
print("Matrix(rows=4, cols=4).Concat(Matrix(rows=2, cols=2))")
print("")
print("Expected:")
print("   1.000     0.000     0.000     0.000     1.000     0.000\n   0.000     1.000     0.000     0.000     0.000     1.000\n   0.000     0.000     1.000     0.000     0.000     0.000\n   0.000     0.000     0.000     1.000     0.000     0.000") 
print("Got:")
print(test5)
