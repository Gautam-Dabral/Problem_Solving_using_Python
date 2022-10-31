
class node :

    def __init__ (self, initval = None):                   # implicitly invoked when object of node is created
        
        self.value = initval
        self.next = None

    def __str__(self):                                      # implicitly invoked by print() function

        selflist = []

        if self.isempty():
            return (str(selflist))
        
        temp = self 
        selflist.append(temp.value)

        while temp.next != None :
            temp = temp.next
            selflist.append(temp.value)

        return (str(selflist))
    
    def isempty (self):

        return (self.value==None)
    
    def append (self , x):                                   # appends a value at the end (Stack implementation)

        if self.isempty():
            self.value = x
        elif self.next == None:
            newnode = node(x)
            self.next = newnode
        else:
            self.next.append(x)

    def insert (self, x):                                    # inserts a new element at the beginning (Queue implementation)

        if self.isempty():
            self.value = x
            return
        
        newnode = node(x)

        self.value , newnode.value = newnode.value , self.value
        self.next , newnode.next = newnode, self.next
        
        return


    def delete (self, x):                                    # deletes the first occurence of x iteratively

        if self.isempty():
            return
        
        if self.value == x:
            if self.next == None:
                self.value = None
            else:
                self.value = self.next.value
                self.next = self.next.next
                return
        
        else:
            if self.next != None:
                self.next.delete(x)
                if self.next.isempty():
                    self.next = self.next.next
            return


        

l = node(5)
l.append(10)
l.append(2.5)
l.append(-8)

print(l)

l.delete(10)
print(l)

for i in range(5,12):
    l.append(i)
print(l)







