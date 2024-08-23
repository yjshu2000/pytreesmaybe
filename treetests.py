#classes???

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def printNode(self):
        print(self.data)

class Tree:
    #constants lol
    SPACING = 3
    
    def __init__(self, root=None):
        self.root = root

    def insert(self, newData):
        if not self.root:
            self.root = TreeNode(newData)
        else:
            self._insert_rec(self.root, newData)

    def _insert_rec(self, node, newData):
        # Example insert logic (modify as needed)
        if newData < node.data:
            if node.left is None:
                node.left = TreeNode(newData)
            else:
                self._insert_rec(node.left, newData)
        else:
            if node.right is None:
                node.right = TreeNode(newData)
            else:
                self._insert_rec(node.right, newData)

    def find(self, query):
        return self._find_rec(self.root, query)

    def _find_rec(self, node, query):
        if node is None:
            return None
        if query == node.data:
            return node.data
        elif query < node.data:
            return self._find_rec(node.left, query)
        else:
            return self._find_rec(node.right, query)

    def printTree(self, form):
        if (form == 1):
            return self._print_rec1(self.root)
        elif (form == 2):
            return self._print_rec2(self.root)
        elif (form == 3):
            return self._print_rec3(self.root)
        elif (form == 4):
            return self._print_rec4(self.root, -1)
        elif (form == 5):
            return self._print_rec5(self.root, -1)
        elif (form == 6):
            return self._print_rec6(self.root, -1, "none")
        elif (form == 7):
            return self._print_rec7(self.root, -1, "none")
        else:
            print("oops")

    def _print_rec1(self, node):
        #prints in traversial order
        if node:
            print(node.data)
            self._print_rec1(node.left)
            self._print_rec1(node.right)

    def _print_rec2(self, node):
        #prints leaves first then parent of those leaves
        if node:
            self._print_rec2(node.left)
            self._print_rec2(node.right)
            print(node.data)

    def _print_rec3(self, node):
        #prints in data order
        if node:
            self._print_rec3(node.left)
            print(node.data)
            self._print_rec3(node.right)

    def _print_rec4(self, node, prevlength):
        #formatted attempt 1: directory listings
        nextlength = 0
        if node:
            if (prevlength >= 0):
                print(' ' * prevlength 
                      + '|' + '-' * self.SPACING 
                      + str(node.data))
                nextlength = prevlength + self.SPACING + 1
            else:
                print(str(node.data))
            self._print_rec4(node.left, nextlength)
            self._print_rec4(node.right, nextlength)

    def _print_rec5(self, node, prevlength):
        #formatted attempt 2: IT'S A REAL TREE WOW!
        if (prevlength >= 0):
            nextlength = prevlength + self.SPACING + 1
        else:
            nextlength = 0
        if node:
            self._print_rec5(node.left, nextlength)
            if (prevlength >= 0):
                print(' ' * prevlength 
                      + '|' + '-' * self.SPACING 
                      + str(node.data))
                #nextlength = prevlength + self.SPACING + 1
            else:
                print(str(node.data))
            self._print_rec5(node.right, nextlength)

    def _print_rec6(self, node, prevlength, prevdir):
        #formatted attempt 3: different left/right symbols
        if (prevlength >= 0):
            nextlength = prevlength + self.SPACING + 1
        else:
            nextlength = 0
        if (prevdir == 'left'):
            dirsym = '┌'
        elif (prevdir == 'right'):
            dirsym = '└'
        else:
            dirsym = ''
        if node:
            self._print_rec6(node.left, nextlength, 'left')
            if (prevlength >= 0):
                print(' ' * prevlength 
                      + dirsym + '-' * self.SPACING 
                      + str(node.data))
            else:
                print(str(node.data))
            self._print_rec6(node.right, nextlength, 'right')

    def _print_rec7(self, node, prevlength, prevdir):
        #formatted attempt 4: different left/right symbols (no unicode)
        if (prevlength >= 0):
            nextlength = prevlength + self.SPACING + 1
        else:
            nextlength = 0
        if (prevdir == 'left'):
            dirsym = '/'
        elif (prevdir == 'right'):
            dirsym = '\\'
        else:
            dirsym = ''
        if node:
            self._print_rec7(node.left, nextlength, 'left')
            if (prevlength >= 0):
                print(' ' * prevlength 
                      + dirsym + '-' * self.SPACING 
                      + str(node.data))
            else:
                print(str(node.data))
            self._print_rec7(node.right, nextlength, 'right')
            


#aaaa




#testing
testnums = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
testnums2 = [21, 14, 28, 7, 17, 8, 12, 11, 24, 32, 19, 16, 5, 31, 18, 9,
             13, 27, 6, 29, 1, 3, 25, 22, 20, 2, 10, 4, 15, 30, 23, 26]
testnums3 = [45, 85, 100, 16, 1, 9, 38, 70, 78, 8, 48, 49, 90, 82, 34,
           91, 59, 64, 51, 63, 39, 72, 10, 2, 20, 21, 56, 40, 31,
           89, 14, 75, 44, 81, 66, 28, 76, 97, 67, 33, 32, 68, 79,
           27, 24, 15, 13, 98, 17, 23, 42, 54, 83, 46, 25, 65, 6,
           18, 30, 47, 88, 5, 58, 99, 3, 37, 74, 69, 11, 29, 86,
           93, 4, 87, 53, 60, 84, 41, 12, 50, 95, 57, 55, 92, 71,
           73, 94, 43, 35, 52, 61, 62, 26, 36, 22, 7, 96, 77, 19, 80]


if __name__ == "__main__":
    #rootNode = TreeNode(testnums3[0])
    testTree = Tree()
    for i in testnums:
        testTree.insert(i)

    #testTree.printTree(1)
    print("\n\n")
    print("format 2:")
    testTree.printTree(2)
    #print(" ")
    #testTree.printTree(3)
    #print("format 4:")
    #testTree.printTree(4)
    #print("\n\n")
    #print("format 5:")
    #testTree.printTree(5)
    print("\n\n")
    print("format 6:")
    testTree.printTree(6)
    print("\n\n")
    print("format 7:")
    testTree.printTree(7)



