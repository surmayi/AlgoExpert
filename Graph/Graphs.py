# Depth First Search in Graph
from collections import deque
class GraphNode:
    def __init__(self,val):
        self.val =val
        self.children=[]

    def addChild(self,child):
        self.children.append(GraphNode(child))
        return self

    def depthFirstSearch(self,res=[]):
        res.append(self.val)
        for child in self.children:
            child.depthFirstSearch(res)
        return res

    def breadthFirstTraversal(self,arr=[]):
        que= deque()
        que.append(self)
        while que:
            size=len(que)
            while size>0:
                node = que.popleft()
                arr.append(node.val)
                size-=1
                for child in node.children:
                    que.append(child)
        return arr



graph =GraphNode('A')
graph.addChild("B").addChild("C").addChild("D")
graph.children[0].addChild("E").addChild("F")
graph.children[2].addChild("G").addChild("H")
graph.children[0].children[1].addChild("I").addChild("J")
graph.children[2].children[0].addChild("K")
print('depthFirstSearch: ',graph.depthFirstSearch())
print('breadthFirstTraversal: ', graph.breadthFirstTraversal())


def single_cycle_check(arr):
    visitedNum=0
    curInd=0
    while visitedNum<len(arr):
        if visitedNum>0 and curInd==0:
            return False
        visitedNum+=1
        curInd = (curInd+ arr[curInd])%len(arr)
        if curInd<0:
            curInd += len(arr)
    return curInd==0


print('single_cycle_check: ', single_cycle_check([2, 3, 1, -4, -4, 2]))



def riverSizes(matrix):
    sizes =[]
    visited = [[False for val in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if visited[i][j]:
                continue
            traverseNode(i,j,matrix,visited,sizes)
    return sizes


def traverseNode(i,j,matrix,visited,sizes):
    curRiverSize=0
    nodesToVisit=[[i,j]]
    while len(nodesToVisit):
        node = nodesToVisit.pop()
        i,j = node[0], node[1]
        if visited[i][j]:
            continue
        visited[i][j]=True
        if matrix[i][j]==0:
            continue
        curRiverSize+=1
        unvisitedNeighbors= getUnivisitedNeighbors(i,j,matrix,visited)
        for node in unvisitedNeighbors:
            nodesToVisit.append(node)
    if curRiverSize>0:
        sizes.append(curRiverSize)

def getUnivisitedNeighbors(i,j,matrix,visited):
    unvisited=[]
    if i>0 and not visited[i-1][j]:
        unvisited.append([i-1,j])
    if i<len(matrix)-1 and not visited[i+1][j]:
        unvisited.append([i+1,j])
    if j>0 and not visited[i][j-1]:
        unvisited.append([i,j-1])
    if j<len(matrix[0])-1 and not visited[i][j+1]:
        unvisited.append([i,j+1])
    return unvisited



matrix = [
  [1, 0, 0, 1, 0],
  [1, 0, 1, 0, 0],
  [0, 0, 1, 0, 1],
  [1, 0, 1, 0, 1],
  [1, 0, 1, 1, 0]
]

print('riverSizes: ', riverSizes(matrix))


# Youngest Common Ancestor
# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def addDescendants(self, *descendants):
        for descendant in descendants:
            descendant.ancestor = self

def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    if not topAncestor or not descendantOne or not descendantTwo:
        return
    level1 = getLevel(topAncestor,descendantOne)
    level2 = getLevel(topAncestor,descendantTwo)
    if level1>level2:
        return getDescendant(descendantOne,descendantTwo,level1-level2)
    return getDescendant(descendantTwo,descendantOne,level2-level1)


def getLevel(topAncestor,node):
    level=0
    while node and node!=topAncestor:
        node=node.ancestor
        level+=1
    return level

def getDescendant(one,two,diff):
    while one and diff>0:
        one=one.ancestor
        diff-=1
    while one!=two:
        one=one.ancestor
        two=two.ancestor
    return one


def new_trees():
    ancestralTrees = {}
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        ancestralTrees[letter] = AncestralTree(letter)
    return ancestralTrees


trees = new_trees()
trees["A"].addDescendants(trees["B"], trees["C"])
trees["B"].addDescendants(trees["D"], trees["E"])
trees["D"].addDescendants(trees["H"], trees["I"])
trees["C"].addDescendants(trees["F"], trees["G"])

print(getYoungestCommonAncestor(trees["A"], trees["E"], trees["I"]).name)


def removeIslands(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    for row in range(rows):
        for col in range(cols):
            rowBorder = True if row in [0, rows-1] else False
            colBorder = True if row in [0,col-1] else False
            border = rowBorder or colBorder
            if not border:
                continue
            if matrix[row][col]!=1:
                continue
            setBorderOnesToTwos(matrix,row,col)

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col]==1:
                matrix[row][col]=0
            if matrix[row][col]==2:
                matrix[row][col]=1
    return matrix


def setBorderOnesToTwos(matrix,row,col):
    stack = [(row,col)]
    while stack:
        row,col = stack.pop()
        if matrix[row][col]!=1:
            continue
        matrix[row][col]=2
        neighbors= getNeighbors(matrix,row,col)
        for row,col in neighbors:
            if matrix[row][col]!=1:
                continue
            stack.append((row,col))

def getNeighbors(matrix,row,col):
    neighbors =[]
    if row >0:
        neighbors.append((row-1,col))
    if row<len(matrix)-1:
        neighbors.append((row+1,col))
    if col>0:
        neighbors.append((row,col-1))
    if col<len(matrix[0])-1:
        neighbors.append((row,col+1))
    return neighbors


input = [
            [1, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 1, 1],
            [0, 0, 1, 0, 1, 0],
            [1, 1, 0, 0, 1, 0],
            [1, 0, 1, 1, 0, 0],
            [1, 0, 0, 0, 0, 1],
        ]

print(removeIslands(input))






















