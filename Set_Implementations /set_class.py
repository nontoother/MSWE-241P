class Node:
    def __init__(self, value):
        self.leftchild = None
        self.rightchild = None
        self.value = value

    def children(self):
        children = []
        if (self.leftchild):
            children = self.leftchild
        if (self.rightchild):
            if not children:
                children = self.rightchild
            else:
                children[1] = self.rightchild
        return children


class Tree:

    def __init__(self):
        self.root = None
        self.sizeOfTree = 0

    def add(self, cNode, value):
        if cNode is None:
            self.root = Node(value)
            self.sizeOfTree += 1
        elif (value < cNode.value):
            if cNode.leftchild:
                self.add(cNode.leftchild, value)
            else:
                cNode.leftchild = Node(value)
                self.sizeOfTree += 1
                return True

        elif (value > cNode.value):
            if cNode.rightchild:
                self.add(cNode.rightchild, value)
            else:
                cNode.rightchild = Node(value)
                self.sizeOfTree += 1
                return True
        else:
            return False

    def contains(self, cNode, value):
        if cNode is None:
            return False
        elif (value < cNode.value):
            if (cNode.leftchild):
                return self.contains(cNode.leftchild, value)
            else:
                return False
        elif (value > cNode.value):
            if cNode.rightchild:
                return self.contains(cNode.rightchild, value)
            else:
                return False
        else:
            return True

    def printTree(self, cNode):
        if cNode is None:
            return
        else:
            print(cNode.value, end=' ')
            self.printTree(cNode.leftchild)
            self.printTree(cNode.rightchild)


class mySet:
    def __init__(self):
        self.sizeOfset = 0
        self.dataset = Tree()

    def add(self, value):
        self.dataset.add(self.dataset.root, value)
        self.sizeOfset = self.dataset.sizeOfTree

    def contains(self, value):
        return self.dataset.contains(self.dataset.root, value)

    def size(self):
        return self.sizeOfset

    def printSet(self):
        self.dataset.printTree(self.dataset.root)