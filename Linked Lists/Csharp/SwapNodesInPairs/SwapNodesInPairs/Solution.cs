using MergeTwoSortedListsNamespace;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//# /*
//#  * Escribe un algoritmo que intercambie parejas de nodos adyacentes sin
//#  * modificar el valor interno de los nodos.
//#  *
//#  * Ejemplo:
//#  *  Input: 1->2->4->6->8
//#  *  Output: 2->1->6->4->8
//#  */

namespace SwapNodesInPairsNamespace
{
    class Solution
    {
        public static Node SwapNodesInPairs(Node head)
        {
            if (head == null || head.Next == null)
                return head;

            Node temp = head.Next.Next;
            head.Next.Next = head;
            head = head.Next;
            head.Next.Next = SwapNodesInPairs(temp);

            return head;
        }
    }
}
