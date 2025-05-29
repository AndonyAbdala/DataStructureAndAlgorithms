//# /*
//#  * Escribe un algoritmo para combinar dos listas enlazadas simples ordenadas.
//#  * El resultado debe ser una única lista enlazada ordenada. Devuelve su head.
//#  *
//#  * Ejemplo:
//#  *  Input: 1->2->4->6, 2->3->5
//#  *  Output: 1->2->2->3->4->5->6
//#  */

using MergeTwoSortedListsNamespace;

class MergeTwoSortedLists
{
    static void Main(string[] args)
    {
        MyLinkedList myLinkedList1 = new MyLinkedList();
        myLinkedList1.AddLast(1);
        myLinkedList1.AddLast(2);
        myLinkedList1.AddLast(4);
        myLinkedList1.AddLast(6);
        myLinkedList1.PrintLinkedList();

        Console.WriteLine();

        MyLinkedList myLinkedList2 = new MyLinkedList();
        myLinkedList2.AddLast(2);
        myLinkedList2.AddLast(3);
        myLinkedList2.AddLast(5);
        myLinkedList2.PrintLinkedList();

        Console.WriteLine();
        MyLinkedList result = Solution.MergeTwoSortedLists(myLinkedList1, myLinkedList2);
        result.PrintLinkedList();
    }
}