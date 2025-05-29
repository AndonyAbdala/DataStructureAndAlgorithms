# /*
#  * Escribe un algoritmo para combinar dos listas enlazadas simples ordenadas.
#  * El resultado debe ser una única lista enlazada ordenada. Devuelve su head.
#  *
#  * Ejemplo:
#  *  Input: 1->2->4->6, 2->3->5
#  *  Output: 1->2->2->3->4->5->6
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


def MergeTwoSortedLists(linkedList1: SingleLinkedList, linkedList2: SingleLinkedList):
    output = SingleLinkedList()
    node = Node(-1)
    auxCurrentNode = node
    linkedList1CurrentNode = linkedList1.head
    linkedList2CurrentNode = linkedList2.head

    while linkedList1CurrentNode != None and linkedList2CurrentNode != None:
        if linkedList1CurrentNode.data <= linkedList2CurrentNode.data:
            auxCurrentNode.next = Node(linkedList1CurrentNode.data)
            linkedList1CurrentNode = linkedList1CurrentNode.next
        else:
            auxCurrentNode.next = Node(linkedList2CurrentNode.data)
            linkedList2CurrentNode = linkedList2CurrentNode.next
        auxCurrentNode = auxCurrentNode.next

    if linkedList1CurrentNode == None and linkedList2CurrentNode != None:
        auxCurrentNode = linkedList2CurrentNode
    else:
        auxCurrentNode.next = linkedList1CurrentNode
    output.head = node.next
    return output

    


linkedList1= SingleLinkedList()
linkedList1.appendToTail(1)
linkedList1.appendToTail(2)
linkedList1.appendToTail(4)
linkedList1.appendToTail(6)

linkedList2= SingleLinkedList()
linkedList2.appendToTail(2)
linkedList2.appendToTail(3)
linkedList2.appendToTail(5)

mergedList = MergeTwoSortedLists(linkedList1, linkedList2)
mergedList.printLinkedList()