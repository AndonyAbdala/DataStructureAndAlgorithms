namespace RemoveDuplicateNodes
{
    class Node
    {
        public int Value;
        public Node? Next;

        public Node(int value)
        {
            this.Value = value;
        }
    }

    class MyLinkedList
    {
        public Node? Head;

        public void AddLast(int value)
        {
            if (this.Head == null)
            {
                this.Head = new Node(value);
                return;
            }

            Node currentNode = this.Head;

            while (currentNode.Next != null)
            {
                currentNode = currentNode.Next;
            }
            currentNode.Next = new Node(value);
        }

        public void PrintLinkedList()
        {
            if (this.Head == null)
            {
                Console.WriteLine("END");
                return;
            }

            Node currentNode = this.Head;
            Console.Write($"{currentNode.Value} -> ");
            while (currentNode.Next != null)
            {
                Console.Write($"{currentNode.Next.Value} -> ");
                currentNode = currentNode.Next;
            }
            Console.WriteLine("END");
        }
    }
}
