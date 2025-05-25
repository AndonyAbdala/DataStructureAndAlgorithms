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

namespace ZeroMatrix;

class ZeroMatrix
{
    static void Main(string[] args)
    {
        int[][] matrix = new int[][]
        {
            new int[] { 2, 1, 3, 0, 2 },
            new int[] { 7, 4, 1, 3, 8 },
            new int[] { 4, 0, 1, 2, 1 },
            new int[] { 9, 3, 4, 1, 9 }
        };

        Solution solution = new Solution();
        solution.zeroMatrixSolution(matrix);
    }
}