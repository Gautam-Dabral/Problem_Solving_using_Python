class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

    def __str__(self):
        return f"{self.value}->"

    def isEmpty(self):
        return self.value == None

class LinkedList:
    def __init__(self):
        self.length = 0
        newNode = Node()
        self.head = newNode
    
    def append(self, value):
        if self.head.isEmpty():
            self.head.value = value 
            return

        newNode = Node(value)
        temp = self.head
        while (temp.next != None):
            temp = temp.next
        temp.next = newNode
        return
    
    def showLast(self):
        temp = self.head
        print(temp, end="")
        while (temp.next != None):
            print(temp.next, end="")
            temp = temp.next


l = LinkedList()
l.append(10)
l.append(20)
l.append(30)
l.append(40)
l.showLast()
