using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RemoveDuplicateNodes
{
    class Solution
    {
        public static void RemoveDuplicateNodes(MyLinkedList linkedList)
        {
            if (linkedList == null || linkedList.Head == null) return;

            HashSet<int> seenValues = new HashSet<int>();
            Node currentNode = linkedList.Head;

            while (currentNode.Next != null)
            {
                if (seenValues.Contains(currentNode.Next.Value))
                {

                   // Remove the duplicate node
                    currentNode.Next = currentNode.Next.Next;
                }
                else
                {
                    seenValues.Add(currentNode.Next.Value);
                    currentNode = currentNode.Next;
                }
            }
        }
    }
}
