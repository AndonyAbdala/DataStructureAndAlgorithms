using MergeTwoSortedListsNamespace;

//# /*
//#  * Escribe un algoritmo que realice la suma de dos listas que representan
//#  * dos enteros positivos. Las listas están en posición invertida.
//#  *
//#  * Ejemplo:
//#  *  Input: 1->2->4, 5->2->8
//#  *  Output: 6->4->2->1
//#  *  6421 + 825 = 7246
//#  */


namespace SumTwoLinkedListsNamespace
{
    class Solution
    {
        public static MyLinkedList SumTwoLinkedLists(MyLinkedList firstList, MyLinkedList secondList)
        {
            // check for empty heads

            Node output = new Node(-1);
            Node currentNodeOutput = output;
            Node currentNode1 = firstList.Head;
            Node currentNode2 = secondList.Head;

            int currentNode1Value;
            int currentNode2Value;

            int acarreo = 0;
            while (currentNode1 != null || currentNode2 != null)
            {
                if (currentNode1 == null)
                    currentNode1Value = 0;
                else
                    currentNode1Value = currentNode1.Value;

                if (currentNode2 == null)
                    currentNode2Value = 0;
                else
                    currentNode2Value = currentNode2.Value;

                int result = currentNode1Value + currentNode2Value + acarreo;
                acarreo = 0;
                if (result > 9)
                {
                    acarreo = 1;
                    result = result - 10;
                }
                currentNodeOutput.Next = new Node(result);

                currentNodeOutput = currentNodeOutput.Next;

                if (currentNode1 != null)
                    currentNode1 = currentNode1.Next;
                if (currentNode2 != null)
                    currentNode2 = currentNode2.Next;
            }

            if (acarreo == 1)
            {
                currentNodeOutput.Next = new Node(1);
            }

            //if (currentNode1 != null && currentNode2 == null)
            //{
            //    while (currentNode1 != null)
            //    {
            //        currentNodeOutput.Next = new Node(currentNode1.Value + acarreo);
            //        acarreo = 0;
            //        currentNodeOutput = currentNodeOutput.Next;
            //        currentNode1 = currentNode1.Next;
            //    }
            //}
            //else
            //{
            //    while (currentNode2 != null)
            //    {
            //        currentNodeOutput.Next = new Node(currentNode2.Value + acarreo);
            //        acarreo = 0;
            //        currentNodeOutput = currentNodeOutput.Next;
            //        currentNode2 = currentNode2.Next;
            //    }
            //}

            MyLinkedList linkedListOutput = new MyLinkedList();
            linkedListOutput.Head = output.Next;

            return linkedListOutput;
        }
    }
}
