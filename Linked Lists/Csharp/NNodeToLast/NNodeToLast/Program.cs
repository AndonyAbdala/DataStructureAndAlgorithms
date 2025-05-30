using MergeTwoSortedListsNamespace;
using NNodeToLastNamespace;

//# /*
//#  * Dada una lista enlazada simple y un valor N, devuelve el nodo N empezando por el final
//#  *
//#  * Ejemplo:
//#  *  Input: 1->2->4->6, 2
//#  *  Output: 4
//#  */

class NNodeToLast
{
    static void Main(string[] args)
    {
        MyLinkedList linkedList = new MyLinkedList();
        linkedList.AddLast(1);
        linkedList.AddLast(5);
        linkedList.AddLast(2);
        linkedList.AddLast(6);
        linkedList.AddLast(1);
        linkedList.AddLast(7);
        linkedList.AddLast(18);
        linkedList.PrintLinkedList();

        Console.WriteLine();
        int result = Solution.NNodeToLast(linkedList.Head, 4);
        Console.WriteLine("El nodo N desde el final es: " + result);
    }
}