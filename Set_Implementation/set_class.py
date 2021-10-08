# Class for linkedlist
class LinkedlistNode():
    # Function to initialise the node
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedlistSet():
    def __init__(self):
        self.head = None
        self.sizeOfSet = 0

    # adds value to linkedlist if value not already in linkedlist
    # returns 1 if value added, or returns 0 if value already present
    def add(self, value):
        curr = self.head

        # base case if self.head == 0
        if curr == None:
            newNode = LinkedlistNode(value)
            self.head = newNode
            self.sizeOfSet = self.sizeOfSet + 1
            return True

        reachedEndOfList = False
        while (curr.value != value):
            temp = curr.next
            if temp == None:  # reached end of linkedlist
                reachedEndOfList = True
                break
            else:
                curr = temp  # go forward

        if reachedEndOfList:  # value not found. insert value here
            newNode = LinkedlistNode(value)
            curr.next = newNode
            self.sizeOfSet = self.sizeOfSet + 1
            return True
        else:  # found existing element with value in linkedlist
            return False

    def contains(self, value):
        curr = self.head

        # base case if self.head == 0
        if curr == None:
            return False

        reachedEndOfList = False
        while (curr.value != value):
            temp = curr.next
            if temp == None:  # reached end of linkedlist
                reachedEndOfList = True
                break
            else:
                curr = temp  # go forward

        if reachedEndOfList:  # value not found. insert value here
            return False
        else:  # found existing element with value in linkedlist
            return True

    # funion of sets
    def find_union(lst1, lst2):
        result_lst = list(set(lst1) | set(lst2))
        return result_lst

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
        if cNode is None:
            self.root = TreeNode(value)
            self.sizeOfTree += 1
        elif (value < cNode.value):
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
        self.maxLength = 10000
        self.length = 0
        self.table = [None] * self.maxLength

    def length(self):
        return self.length

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
            if self.table[cur_pos]:  # something exists at this location
                if self.table[cur_pos] == key:  # duplicate
                    return False
                else:
                    cur_pos += 1  # linear probing
            else:
                self.table[cur_pos] = key  # add key when nothing found at cur_pos
                self.length += 1
                return True

            if cur_pos == initial_pos:  # if one cycle done, then break
                print('hashtable is full. increase space')
                return False

    def contains(self, key):
        hashval = self.hashing(key)
        initial_pos = hashval
        cur_pos = hashval
        while (True):
            if self.table[cur_pos]:  # something exists at this location
                if self.table[cur_pos] == key:  # found key/value
                    return True
                else:
                    cur_pos += 1  # keep linear probing
            else:
                return False  # nothing found at this location. key absent

            if cur_pos == initial_pos:  # if one cycle done, then break
                print('hashtable is full. increase space')
                return False

    def printHashTable(self):
        for i in range(self.maxLength):
            if self.table[i]:
                print(self.table[i], end=" ")

    def mySet(self, key, value):
        self.length += 1
        self.key = self.key(key)

    def get(self, key):
        index = self.findNumber(key)
        return self.table[index][1]

    def delNumber__(self, key):
        index = self.findNumber(key)
        self.table[index] = None

    def incr_key(self, key):
        return (key + 1) % self.max_length


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

