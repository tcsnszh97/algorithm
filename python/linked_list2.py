class Node:
    def __init__(self,initdata):
        self.data= initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        if self.head == None:
            self.head = Node(item)
        else:
            current = self.head
            while current.getNext() != None:
                current = current.getNext()
            current.setNext(Node(item))

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext
        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext
        else:
            previous.setNext(current.getNext())

    def show(self):
        current = self.head
        while current != None:
            print(current.getData())
            current = current.getNext()

if __name__ == '__main__':
    mylist = UnorderedList()
    mylist.show()
    mylist.add(31)
    mylist.add(77)
    mylist.add(17)
    mylist.add(93)
    mylist.add(26)
    mylist.add(54)
    mylist.show()