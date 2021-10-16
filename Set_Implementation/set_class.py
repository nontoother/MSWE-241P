# Class for linkedlist
class LinkedlistNode():
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedlistSet():
    def __init__(self):
        self.head = None
        self.sizeOfSet = 0

    def add(self, value):
        curr = self.head

        if curr == None:  # the first Node
            newNode = LinkedlistNode(value)
            self.head = newNode
            self.sizeOfSet = self.sizeOfSet + 1
            return True

        reachedEndOfList = False
        while (curr.value != value):
            temp = curr.next
            if temp == None:
                reachedEndOfList = True
                break
            else:
                curr = temp

        if reachedEndOfList:  # add new node
            newNode = LinkedlistNode(value)
            curr.next = newNode
            self.sizeOfSet = self.sizeOfSet + 1
            return True
        else:
            return False

    def contains(self, value):
        curr = self.head

        if curr == None:
            return False

        reachedEndOfList = False
        while (curr.value != value):
            temp = curr.next
            if temp == None:  # the end not found
                reachedEndOfList = True
                break
            else:
                curr = temp

        if reachedEndOfList:  # value not found. insert value here
            return False
        else:  # found the existed value
            return True

    def printSet(self):
        curhead = self.head
        print(end='\n')

        while (curhead):
            print(curhead.value, end=' ')
            curhead = curhead.next
        print('\n')

    def size(self):
        return self.sizeOfSet


# Class for binary tree
class TreeNode:
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
        if cNode is None:  # already find the right place to insert new node
            self.root = TreeNode(value)
            self.sizeOfTree += 1
        elif (value < cNode.value):  # decide which path should go
            if cNode.leftchild:
                self.add(cNode.leftchild, value)
            else:
                cNode.leftchild = TreeNode(value)
                self.sizeOfTree += 1
                return True

        elif (value > cNode.value):
            if cNode.rightchild:
                self.add(cNode.rightchild, value)
            else:
                cNode.rightchild = TreeNode(value)
                self.sizeOfTree += 1
                return True
        else:
            return False

    def contains(self, cNode, value):
        if cNode is None:  # did not find the value in the right place
            return False
        elif (value < cNode.value):  # recursion to find the right place
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


class TreeSet:
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


# Class for Hash Table
class HashTable(object):

    def __init__(self):
        self.maxLength = 10000  # avoid collision
        self.length = 0
        self.table = [None] * self.maxLength

    def length(self):
        return self.length

    # hash function
    def hashing(self, key):
        keystr = str(key)  # make sure key is converted to string
        keylen = len(keystr)
        x = 26
        hashval = 0
        for i in range(keylen):
            hashval = x ** i + ord(keystr[i])

        return hashval % self.maxLength

    def insert(self, key):
        hashval = self.hashing(key)
        initial_pos = hashval
        cur_pos = hashval
        while (True):
            if self.table[cur_pos]:  # get same value from hash function
                if self.table[cur_pos] == key:  # duplicate
                    return False
                else:
                    cur_pos += 1  # linear probing
            else:
                self.table[cur_pos] = key  # add key when the place is empty
                self.length += 1
                return True

            if cur_pos == initial_pos:
                print('hashtable is full. increase space')
                return False

    def contains(self, key):
        hashval = self.hashing(key)
        initial_pos = hashval
        cur_pos = hashval
        while (True):
            if self.table[cur_pos]:
                if self.table[cur_pos] == key:  # found key
                    return True
                else:
                    cur_pos += 1  # searching in linear probing
            else:
                return False  # nothing found

            if cur_pos == initial_pos:  # no place
                print('hashtable is full. increase space')
                return False

    def printHashTable(self):
        for i in range(self.maxLength):
            if self.table[i]:
                print(self.table[i], end=" ")


class HashTableSet:
    def __init__(self):
        self.sizeOfset = 0
        self.dataset = HashTable()

    def add(self, value):
        self.dataset.insert(value)
        self.sizeOfset = self.dataset.length

    def contains(self, value):
        return self.dataset.contains(value)

    def size(self):
        return self.dataset.length

    def printSet(self):
        self.dataset.printHashTable()

