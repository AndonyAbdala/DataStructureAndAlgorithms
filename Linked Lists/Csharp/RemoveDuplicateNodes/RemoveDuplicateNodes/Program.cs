using RemoveDuplicateNodes;

//# /*
//#  * Escribe un algoritmo para eliminar los elementos duplicados en una Lista enlazada
//#  *
//#  * Ejemplo:
//#  *  Input: 1->2->2->3->4->1
//#  *  Output: 1->2->3->4
//#  *
//#  *
//#  *
//#  * Follow-up: ¿Cuál sería tu solución si no pudieras utilizar memoria adicional?
//#  */

class RemoveDuplicateNoodes
{
    static void Main(string[] args)
    {
        // Create a linked list with duplicate nodes
        MyLinkedList linkedList = new MyLinkedList();
        linkedList.AddLast(1);
        linkedList.AddLast(2);
        linkedList.AddLast(2);
        linkedList.AddLast(3);
        linkedList.AddLast(3);
        linkedList.AddLast(4);
        linkedList.PrintLinkedList();

        Solution.RemoveDuplicateNodes(linkedList);

        linkedList.PrintLinkedList();


        //Console.WriteLine("Original Linked List:");
        //PrintLinkedList(linkedList);

        //// Remove duplicates
        //RemoveDuplicates(linkedList);

        //Console.WriteLine("Linked List after removing duplicates:");
        //PrintLinkedList(linkedList);
    }
}