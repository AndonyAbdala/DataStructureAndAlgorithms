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

linkedList = SingleLinkedList()
linkedList.appendToTail(1)
linkedList.appendToTail(2)
linkedList.appendToTail(3)
linkedList.printLinkedList()
linkedList.appendToTail(4)
linkedList.appendToTail(5)
linkedList.appendToTail(6)
linkedList.printLinkedList()
linkedList.deleteNode(1)
linkedList.printLinkedList()
linkedList.deleteNode(3)
linkedList.printLinkedList()
linkedList.deleteNode(6)
linkedList.printLinkedList()