using MergeTwoSortedListsNamespace;
//# /*
//#  * Dada una lista enlazada simple y un valor N, devuelve el nodo N empezando por el final
//#  *
//#  * Ejemplo:
//#  *  Input: 1->2->4->6, 2
//#  *  Output: 4
//#  */

namespace NNodeToLastNamespace
{
    class Solution
    {
        public static int NNodeToLast(Node head, int n)
        {
            Node aux1 = head;
            Node aux2 = head;

            for (int i = 0; i < n; i++)
            {
                aux1 = aux1.Next;
                if (aux1 == null)
                    Console.WriteLine("Position is out of range");
            }
                
            while (aux1 != null)
            {
                aux1 = aux1.Next;
                aux2 = aux2.Next;
            }
                
            return aux2.Value;
        }
    }
}
