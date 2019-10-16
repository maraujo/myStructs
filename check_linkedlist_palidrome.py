class Node():
    def __init__(self):
        self.value = None
        self.next = None

    def setNext(self, nxt):
        self.next = nxt

    def getNext(self):
        return self.next

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

# Generating Linked List
# "a"<->"b"<->"a"
n1 = Node()
n2 = Node()
n3 = Node()
n4 = Node()
n5 = Node()

head = n1

n1.setValue("a")
n2.setValue("b")
n3.setValue("asda")
n4.setValue("b")
n5.setValue("a")

n1.setNext(n2)
n2.setNext(n3)
n3.setNext(n4)
n4.setNext(n5)

def printLinkedList(head):
    current_node = head
    print("Printing List")
    while current_node != None:
        print(current_node.getValue())
        current_node = current_node.getNext()

printLinkedList(head)

def checkPalidrome(head):
    # Empty list case
    if head == None:
        return False
    # Single item case
    if head.getNext() == None:
        return True

    #Insert items in a python list
    items = []
    current_node = head
    while current_node != None:
        items.append(current_node.getValue())
        current_node = current_node.getNext()

    
    #Check palidrome
    begin = 0
    end = len(items) -1
    #ex1: [a,b,b,a]
    #ex2: [a,b,X,b,a]
    while begin < end:
        if items[begin] != items[end]:
            return False
        begin += 1
        end -= 1
    return True

print(checkPalidrome(head))






