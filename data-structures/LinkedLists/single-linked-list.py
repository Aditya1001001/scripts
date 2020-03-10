class Node:
    def __init__(self, value):
        self.data = value
        self.link = None

class SingleLinkedList:

    def __init__(self):
        self.start = None
    
    def display(self):
        if self.start == None:
            print("List is empty")
            return -1
        else:
            p = self.start
            while p is not None:
                print(p.data)
                p = p.link
            print()
    
    def count_nodes(self):
        n=0
        if self.start == None:
            print("List is empty")
            return 0
        else:
            p = self.start
            while p is not None:
                n+=1
                p = p.link
            return n

    def search(self, x):
        if self.start == None:
            print("List is empty")
            return -1
        p = self.start
        pos = 1
        while p is not None:
            if p.data == x:
                return pos
            pos +=1
            p = p.link
        else:
            return -1

    def insert_at_start(self, data):
        new_node = new Node(data)
        if self.start == None:
            self.start = new_node
        else:
            new_node.link = self.start 
        self.start = new_node

    def insert_at_end(self, data):
        new_node = new Node(data)
        if self.start == None:
            self.start = new_node
        else:
            p = self.start
            while not p.link == None:
                p = p.link
            else:
                p.link = new_node

    def insert_before(self, data, x)
        
     