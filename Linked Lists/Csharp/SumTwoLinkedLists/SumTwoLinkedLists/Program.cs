using MergeTwoSortedListsNamespace;

using SumTwoLinkedListsNamespace;
class SumTwoLinkedList
{
    static void Main(string[] args)
    {
        MyLinkedList myLinkedList1 = new MyLinkedList();
        myLinkedList1.AddLast(4);
        myLinkedList1.AddLast(6);
        myLinkedList1.AddLast(7);
        myLinkedList1.AddLast(7);
        myLinkedList1.PrintLinkedList();

        Console.WriteLine();

        MyLinkedList myLinkedList2 = new MyLinkedList();
        myLinkedList2.AddLast(3);
        myLinkedList2.AddLast(7);
        myLinkedList2.AddLast(8);
        myLinkedList2.PrintLinkedList();

        Console.WriteLine();

        Solution.SumTwoLinkedLists(myLinkedList1, myLinkedList2).PrintLinkedList();
    }
}