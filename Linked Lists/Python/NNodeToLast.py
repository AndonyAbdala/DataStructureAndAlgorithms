# /*
#  * Dada una lista enlazada simple y un valor N, devuelve el nodo N empezando por el final
#  *
#  * Ejemplo:
#  *  Input: 1->2->4->6, 2
#  *  Output: 4
#  */

class Node:
    def __init__(self, data: int = None):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def appendNodeToTail(self, node: Node):
        if (self.head == None):
            self.head.next = node
            return
        
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = node

    def appendToTail(self, value: int):
        if (self.head == None):
            self.head = Node(value)
            return
        
        currentNode = self.head
        while currentNode.next != None:
            currentNode = currentNode.next
        currentNode.next = Node(value)

    def deleteNode(self, value: int):
        if self.head == None:
            return
        
        currentNode = self.head
        if self.head.data == value:
            self.head = currentNode.next
            return
        
        while currentNode.next != None:
            if currentNode.next.data == value:
                currentNode.next = currentNode.next.next
                return
            currentNode = currentNode.next

    def printLinkedList(self):
        if self.head == None:
            print("END")
            return
        currentNode = self.head
        while currentNode.next != None:
            print(f"{currentNode.data} -> ", end="")
            currentNode = currentNode.next
        print(f"{currentNode.data} -> END")

def NNodeToLast(head: Node, n: int):
    aux1 = head
    aux2 = head

    for i in range(n):
        aux1 = aux1.next

    while aux1 != None:
        aux1 = aux1.next
        aux2 = aux2.next

    return aux2.data

linkedList = SingleLinkedList()
linkedList.appendToTail(4)
linkedList.appendToTail(1)
linkedList.appendToTail(2)
linkedList.appendToTail(4)
linkedList.appendToTail(6)
linkedList.appendToTail(5)
linkedList.appendToTail(6)
linkedList.appendToTail(8)
linkedList.appendToTail(1)
linkedList.printLinkedList()

result = NNodeToLast(linkedList.head, 4)
print(result)