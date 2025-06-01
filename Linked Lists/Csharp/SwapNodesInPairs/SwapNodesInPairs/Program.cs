using MergeTwoSortedListsNamespace;
using SwapNodesInPairsNamespace;

class SwapNodesInPairs
{
    static void Main(string[] args)
    {
        MyLinkedList myLinkedList = new MyLinkedList();
        myLinkedList.AddLast(1);
        myLinkedList.AddLast(2);
        myLinkedList.AddLast(4);
        myLinkedList.AddLast(6);
        myLinkedList.AddLast(8);
        myLinkedList.PrintLinkedList();

        Node result = Solution.SwapNodesInPairs(myLinkedList.Head);
    }
}