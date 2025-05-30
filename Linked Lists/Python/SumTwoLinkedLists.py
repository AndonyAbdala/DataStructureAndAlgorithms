# /*
#  * Escribe un algoritmo que realice la suma de dos listas que representan
#  * dos enteros positivos. Las listas están en posición invertida.
#  *
#  * Ejemplo:
#  *  Input: 1->2->4, 5->2->8
#  *  Output: 6->4->2->1
#  *  6421 + 825 = 7246
#  */

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

def SumTwoLinkedLists(linkedList1: SingleLinkedList, linkedList2: SingleLinkedList):
    result = Node(-1)
    currentResultNode = result

    currentNode1 = linkedList1.head
    currentNode2 = linkedList2.head

    acarreo = 0

    while currentNode1 != None and currentNode2 != None:
        resultSum = currentNode1.data + currentNode2.data

        resultSum = resultSum + acarreo
        acarreo = 0

        if resultSum > 9:
            acarreo = 1
            resultSum = resultSum - 10

        currentResultNode.next = Node(resultSum)
        currentResultNode = currentResultNode.next

        currentNode1 = currentNode1.next
        currentNode2 = currentNode2.next

    if currentNode1 != None and currentNode2 == None:
        while currentNode1 != None:
            currentResultNode.next = Node(currentNode1.data + acarreo)

            acarreo = 0
            currentNode1 = currentNode1.next
            currentResultNode = currentResultNode.next
    else:
        while currentNode2 != None:
            currentResultNode.next = Node(currentNode2.data + acarreo)
            auxCurrentNode = auxCurrentNode.next

            acarreo = 0
            currentNode1 = currentNode2.next
            currentResultNode = currentResultNode.next

    resultList = SingleLinkedList()
    resultList.head = result.next
    return resultList

linkedList1= SingleLinkedList()
linkedList1.appendToTail(1)
linkedList1.appendToTail(2)
linkedList1.appendToTail(4)
linkedList1.appendToTail(6)
linkedList1.printLinkedList()

linkedList2= SingleLinkedList()
linkedList2.appendToTail(2)
linkedList2.appendToTail(9)
linkedList2.appendToTail(5)
linkedList2.printLinkedList()

result = SumTwoLinkedLists(linkedList1, linkedList2)
result.printLinkedList()