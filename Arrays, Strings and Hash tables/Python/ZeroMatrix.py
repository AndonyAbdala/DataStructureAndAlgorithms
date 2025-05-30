# /*
#  * Dada una matriz, escribe un algoritmo para establecer ceros en la fila F y columna C si existe un
#  * 0 en la celda F:C
#  *
#  * Ejemplo:
#  *  Input: 2 1 3 0 2
#  *         7 4 1 3 8
#  *         4 0 1 2 1
#  *         9 3 4 1 9
#  *
#  *  Output: 0 0 0 0 0
#  *          7 0 1 0 8
#  *          0 0 0 0 0
#  *          9 0 4 0 9
#  */

def checkIfFirstRowHasZero(matrix):
    for rowItem in matrix[0]:
        if rowItem == 0:
            return True
    return False
    

def checkIfFirstColumnHasZero(matrix):
    for index, row in enumerate(matrix):
        if row[0] == 0:
            return True
    return False

def checkForZeros(matrix):
    for rowIndex, row in enumerate(matrix):
        if rowIndex == 0:
            continue
        for columnIndex, item in enumerate(row):
            if columnIndex == 0:
                continue
            if item == 0:
                matrix[0][columnIndex] = 0
                matrix[rowIndex][0] = 0

def setRowToZero(matrix, row):
    for columnIndex, _ in enumerate(matrix[0]):
        matrix[row][columnIndex] = 0

def setColumnToZero(matrix, column):
    for rowIndex, _ in enumerate(matrix):
        matrix[rowIndex][column] = 0

def processRows(matrix):
    for rowIndex, _ in enumerate(matrix):
        if matrix[rowIndex][0] == 0:
            setRowToZero(matrix, rowIndex)

def processColumn(matrix):
    for columnIndex, row in enumerate(matrix[0]):
        if matrix[0][columnIndex] == 0:
            setColumnToZero(matrix, columnIndex)
         

matrix = [[2, 1, 3, 0, 2], [7, 4, 1, 3, 8], [4, 0, 1, 2, 1], [9, 3, 4, 1, 9]]

firstColumnHasZero = checkIfFirstColumnHasZero(matrix)
firstRowHasZero = checkIfFirstRowHasZero(matrix)
checkForZeros(matrix)
processRows(matrix)
processColumn(matrix)

if firstColumnHasZero:
    setColumnToZero(matrix, 0)

if firstRowHasZero:
    setRowToZero(matrix, 0)


print(matrix)