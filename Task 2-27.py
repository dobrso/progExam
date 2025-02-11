def multiplyMatrix(matrix, number):
    return [[element * number for element in row] for row in matrix]

# Возможно я не так понял задание матрицы, но
def matrixInputTwoLists():
    firstList = list(map(int, input("Введите элементы первого списка через пробел: \n").split()))
    secondList = list(map(int, input("Введите элементы второго списка через пробел: \n").split()))
    return [firstList, secondList]

def matrixInputOneList():
    matrixElements = list(map(int, input("Введите элементы для матрицы через пробел: \n").split()))
    return [matrixElements[:len(matrixElements) // 2], matrixElements[len(matrixElements) // 2:]]

print(f"Умножение матрицы, заданной двумя списками: {multiplyMatrix(matrixInputTwoLists(), 4)}")
print(f"Умножение матрицы, заданной одним списком: {multiplyMatrix(matrixInputOneList(), 4)}")