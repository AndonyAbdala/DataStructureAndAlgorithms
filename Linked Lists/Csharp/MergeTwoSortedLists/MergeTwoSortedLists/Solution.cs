namespace MergeTwoSortedListsNamespace
{
    class Solution
    {
        public static MyLinkedList MergeTwoSortedLists(MyLinkedList linkedList1, MyLinkedList linkedList2)
        {
            MyLinkedList output = new MyLinkedList();
            Node aux = new Node(-1);
            Node auxCurrentNode = aux;

            // Consider cases when linkedList1.Head or linkedList2.Head are null
            Node currentNode1 = linkedList1.Head;
            Node currentNode2 = linkedList2.Head;
            while (currentNode1 != null && currentNode2 != null)
            {
                if (currentNode1.Value <= currentNode2.Value)
                {
                    auxCurrentNode.Next = currentNode1;
                    currentNode1 = currentNode1.Next;
                }
                else
                {
                    auxCurrentNode.Next = currentNode2;
                    currentNode2 = currentNode2.Next;
                }
                auxCurrentNode = auxCurrentNode.Next;
            }

            if (currentNode1 != null && currentNode2 == null)
                auxCurrentNode.Next = currentNode1;
            else
                auxCurrentNode.Next = currentNode2;
            output.Head = aux.Next;
            return output;
        }
    }
}
