using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//# /*
//#  * Dada una matriz, escribe un algoritmo para establecer ceros en la fila F y columna C si existe un
//#  * 0 en la celda F:C
//#  *
//#  * Ejemplo:
//#  *  Input: 2 1 3 0 2
//#  *         7 4 1 3 8
//#  *         4 0 1 2 1
//#  *         9 3 4 1 9
//#  *
//#  *  Output: 0 0 0 0 0
//#  *          7 0 1 0 8
//#  *          0 0 0 0 0
//#  *          9 0 4 0 9
//#  */

namespace ZeroMatrix
{
    class Solution
    {

        public void zeroMatrixSolution(int[][] matrix)
        {
            bool firstRowHasZero = checkIfFirstRowHasZero(matrix);
            bool firstColumnHasZero = checkIfFirstColumnHasZero(matrix);

            searchForZeros(matrix);
            processColumns(matrix);
            processRows(matrix);

            if (firstColumnHasZero)
                setColumnToZero(matrix, 0);

            if (firstRowHasZero)
                setRowToZero(matrix, 0);
        }
        private bool checkIfFirstColumnHasZero(int[][] matrix)
        {
            for (int i = 0; i < matrix.Length; i++)
                if (matrix[i][0] == 0) return true;
            return false;
        }

        private bool checkIfFirstRowHasZero(int[][] matrix)
        {
            for (int i = 0; i < matrix[0].Length; i++)
                if (matrix[0][i] == 0) return true;
            return false;
        }

        private void searchForZeros(int[][] matrix)
        {
            for (int rowIndex = 1; rowIndex < matrix.Length; rowIndex++)
            {
                for (int columnIndex = 1; columnIndex < matrix.Length; columnIndex++)
                {
                    if (matrix[rowIndex][columnIndex] == 0)
                    {
                        matrix[rowIndex][0] = 0;
                        matrix[0][columnIndex] = 0;
                    } 
                }
            }
        }

        private void setColumnToZero(int[][] matrix, int column) 
        { 
            for (int i = 0; i < matrix.Length; i++)
                matrix[i][column] = 0;
        }

        private void setRowToZero(int[][] matrix, int row)
        {
            for (int i = 0; i < matrix[0].Length; i++)
                matrix[row][i] = 0;
        }

        private void processRows(int[][] matrix)
        {
            for(int i = 0; i < matrix.Length; i++)
            {
                if (matrix[i][0] == 0)
                    setRowToZero(matrix, i);
            }
        }

        private void processColumns(int[][] matrix)
        {
            for (int i = 0; i < matrix[0].Length; i++)
            {
                if (matrix[0][i] == 0)
                    setColumnToZero(matrix, i);
            }
        }
    }
}
