# /*
#  * Escribe un algoritmo para eliminar los elementos duplicados en una Lista enlazada
#  *
#  * Ejemplo:
#  *  Input: 1->2->2->3->4->1
#  *  Output: 1->2->3->4
#  *
#  *
#  *
#  * Follow-up: ¿Cuál sería tu solución si no pudieras utilizar memoria adicional?
#  */


class Node:
    def __init__(self, data: int = None):
        self.data = data
        self.next = None



class SingleLinkedList:
    def __init__(self):
        self.head = None

    def clone(self):
        cloneLinkedList = SingleLinkedList()

        if self.head == None:
            return None
        cloneLinkedList.head = self.head
        while currentNode.next != None:
            print(f"{currentNode.data} -> ", end="")
            currentNode = currentNode.next
        print(f"{currentNode.data} -> END")

        return 

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
        
        if self.head.data == value:
            self.head = self.head.next
            return

        currentNode = self.head
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


def removeDuplicatedNodes(linkedList: SingleLinkedList):
    if linkedList == None or linkedList.head == None:
        return
    unique_values = set()
    currentNode = linkedList.head
    unique_values.add(currentNode.data)

    while currentNode != None and currentNode.next != None:
        if currentNode.next.data in unique_values:
            currentNode.next = currentNode.next.next
        else:
            unique_values.add(currentNode.next.data)
            currentNode = currentNode.next

linkedList = SingleLinkedList()
linkedList.appendToTail(2)
linkedList.appendToTail(3)
linkedList.appendToTail(4)
linkedList.appendToTail(7)
linkedList.appendToTail(2)
linkedList.appendToTail(4)
linkedList.appendToTail(2)
linkedList.appendToTail(9)
linkedList.printLinkedList()

removeDuplicatedNodes(linkedList)
linkedList.printLinkedList()
