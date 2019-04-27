class Node ():
    def __init__ (self, value):
        self.value = value
        self.right = None
        self.left = None

    def add (self, value):
        if value < self.value:
            if self.left == None:
                self.left = value
            else:
                self.left.add(value)
        else:
            if self.right == None:
                self.right = value
            else:
                self.right.add(value)

node0 = Node(1)
node1 = node0.add(12)
node2 = node0.add(14)
