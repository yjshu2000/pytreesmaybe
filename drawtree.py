import tkinter as tk
from math import sqrt, floor, ceil
import time

#im putting classes here anyway smh I just want everything here :p

class TreeNode:
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def printNode(self):
        print(self.data)

class Tree:
    #constants lol
    SPACING = 3
    
    def __init__(self, root = None):
        self.root = root

    def insert(self, newData):
        if not self.root:
            self.root = TreeNode(newData)
        else:
            self._insert_rec(self.root, newData)

    def _insert_rec(self, node, newData):
        if newData < node.data:
            if node.left is None:
                node.left = TreeNode(newData, parent = node)
            else:
                self._insert_rec(node.left, newData)
        else:
            if node.right is None:
                node.right = TreeNode(newData, parent = node)
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

    #returns None if not found; returns node's data if deleted
    def delNode(self, query):
        return self._delNode_rec(self.root, query)

    def _delNode_rec(self, node, query):
        if node is None:
            return None
        if query == node.left.data:
            #frick. we need to recursively check for children
            #and move node up...
            node.left = None
            return query
        elif query == node.right.data:
            node.right = None
            return query
        elif query < node.data:
            return self._delNode_rec(node.left, query)
        else:
            return self._delNode_rec(node.right, query)
        

    def printTree(self):
        return self._print_rec(self.root, -1, "none")


    def _print_rec(self, node, prevlength, prevdir):
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
            self._print_rec(node.left, nextlength, 'left')
            if (prevlength >= 0):
                print(' ' * prevlength 
                      + dirsym + '-' * self.SPACING 
                      + str(node.data))
            else:
                print(str(node.data))
            self._print_rec(node.right, nextlength, 'right')

#just realized we never used this lol woops. should we have? maybe?
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#we never used this either. maybe this could've been better than using the weird nested tuple.
class CircleNode:
    def __init__(self, node, coords):
        self.node = node
        self.coords = coords

#make tree with coords... doesn't draw it
class GraphicTree:
    def __init__(self, tree, xspacer, yspacer, x_first, y_root):
        self.tree = tree
        self.xspacer = xspacer
        self.yspacer = yspacer
        self.x = x_first
        self.y_root = y_root
        #when replacing tree data:
        # node.data[0] is the number,
        # node.data[1][0] is x, node.data[1][1] is y.
        #  eg: (12, (100, 200))
        self.makeCoords()

    def makeCoords(self):
        self._makecoords_rec(self.tree.root, self.y_root)

    def _makecoords_rec(self, node, y):
        if node:
            newy = y + self.yspacer
            self._makecoords_rec(node.left, newy)
            node.data = (node.data, (self.x, y))
            self.x += self.xspacer
            self._makecoords_rec(node.right, newy)

class TreeDrawer:
    def __init__(self, canvas, graphictree, circrad = 20,
                 circolour = "lightblue", fontsize = 14, delays = 0):
        self.canvas = canvas
        self.tree = graphictree.tree
        self.r = circrad
        self.circolour = circolour
        self.fontsize = fontsize
        self.delays = delays
        self.drawfromtree()

    def drawfromtree(self):
        self._drawfromtree_rec(self.tree.root)

    def _drawfromtree_rec(self, node):
        r = self.r
        wait = self.delays
        if node:
            x = node.data[1][0]
            y = node.data[1][1]
            label = node.data[0]
            self.canvas.create_oval(x-r, y-r, x+r, y+r,
                                    fill = self.circolour)
            self.canvas.create_text(x, y, text = (label),
                                    font=("Consolas", self.fontsize))
            if node.parent: #draw connectors
                xp = node.parent.data[1][0]
                yp = node.parent.data[1][1]
                magn = sqrt((xp - x)**2 + (yp - y)**2)
                xr = x + r * (xp - x) / magn
                yr = y + r * (yp - y) / magn
                xpr = xp - r * (xp - x) / magn
                ypr = yp - r * (yp - y) / magn
                self.canvas.create_line(xpr, ypr, xr, yr, width = 2,
                                        arrow=tk.LAST, arrowshape = (r/4, r/2, r/4))
            if wait:
                time.sleep(wait)
                root.update()
            self._drawfromtree_rec(node.left)
            self._drawfromtree_rec(node.right)
            
        


############################################################
#stuff to actually run
WIDTH = 1800
HEIGHT = 800
BGCOLOUR = 'lightgrey'

#test stuff for now
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
testnums4 = [
    55, 11, 73, 56, 63, 3, 12, 40, 8, 53,
    44, 83, 4, 71, 24, 58, 32, 70, 99, 52,
    94, 26, 37, 66, 41, 16, 30, 17, 100, 72,
    39, 96, 20, 22, 62, 87, 88, 45, 1, 85,
    47, 51, 15, 82, 95, 14, 79, 68, 92, 60,
    5, 38, 23, 89, 50, 90, 86, 36, 29, 13,
    84, 97, 27, 19, 25, 49, 10, 54, 33, 76,
    98, 77, 64, 42, 18, 93, 74, 35, 67, 6,
    91, 61, 57, 2, 31, 48, 75, 81, 80, 78,
    7, 43, 69, 28, 46, 9, 21, 59, 34, 65]
testnums5 = [19, 5, 28, 17, 16, 24, 25, 20, 30, 13, 23, 15,
             4, 7, 8, 6, 9, 29, 11, 27, 22, 2, 3, 18, 26,
             21, 1, 32, 12, 14, 31, 10]
testnums6 = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1,
             3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 32]


atree = Tree()
for i in testnums6:
    atree.insert(i)

#deletion test
#atree.delNode(24)

#=radius?
scaler = 20

grtr = GraphicTree(atree, xspacer = scaler * 1.5, yspacer = scaler * 4,
                   x_first = scaler * 3, y_root = scaler * 3)
#print(grtr.nodescoords)
#atree.printTree()
#for i in grtr.connectors:
#    print(i)



# Create the main window
root = tk.Tk()
root.title("Tree Drawer")

# Create a shared Canvas widget
canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = BGCOLOUR)
canvas.pack()

# Create and start the tree drawer
app = TreeDrawer(canvas, grtr, fontsize = ceil(scaler * 2/3), circrad = scaler,
                 delays = 0)



# Start the Tkinter event loop
root.mainloop()

