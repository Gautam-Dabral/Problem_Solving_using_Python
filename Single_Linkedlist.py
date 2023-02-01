class Node ():
    def __init__(self, value=None):
        self.value = value
        self.next = None
    def __repr__(self):
        return f"{self.value}->"
    
class LinkedList ():
    def __init__(self, value=None):
        self.node = Node(value)
    def push (self, value):
        new_node = Node(value=value)
        self.node.next = new_node
    def pop (self):
        if self.node.next == None:
            self.node.value = None
    def print_list (self):
        while self.node.next != None:
            print(f"{self.node.value}->", end=" ")
            

l = LinkedList()
l.push(3)
l.push(4)
print(l)
