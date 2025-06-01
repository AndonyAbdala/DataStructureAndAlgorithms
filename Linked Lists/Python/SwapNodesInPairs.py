class Node:
    def __init__(self, data: int = None):
        self.data = data
        self.next = None



class SingleLinkedList:
    def __init__(self):
        self.head = None

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


# /*
#  * Escribe un algoritmo que intercambie parejas de nodos adyacentes sin
#  * modificar el valor interno de los nodos.
#  *
#  * Ejemplo:
#  *  Input: 1->2->4->6->8
#  *  Output: 2->1->6->4->8
#  */

def SwapNodesInPairs(head: Node):
    if head == None or head.next == None:
        return head
    
    temp = head.next.next
    head.next.next = head
    head = head.next
    head.next.next = SwapNodesInPairs(temp)
    return head

def BuildLinkedList(head: Node):
    result = SingleLinkedList()
    currentNode = head
    while currentNode != None:
        result.appendToTail(currentNode.data)
        currentNode = currentNode.next
    return result

linkedList = SingleLinkedList()
linkedList.appendToTail(1)
linkedList.appendToTail(2)
linkedList.appendToTail(4)
linkedList.appendToTail(6)
linkedList.appendToTail(8)
linkedList.printLinkedList()
result = SwapNodesInPairs(linkedList.head)
myNewLinkedList = BuildLinkedList(result)
myNewLinkedList.printLinkedList()


