"""User Defined Data Structures

07/19/20, Peiheng Li (jdlph@hotmail.com)
"""


class Node:
    
    def __init__(self, nodeID, nodeIDEXT):
        # internal node id used for sp calculation
        self.id = nodeID
        # external node id defined by user or input file
        self.idEXT = nodeIDEXT
        self.outgoingLinks = []
    
    def AddOutgoingLinks(self, linkID):
        self.outgoingLinks.append(linkID)
    
    def GetOutgoingLinks(self):
        return self.outgoingLinks

    def GetOutgoingLinksIter(self):
        for i in self.outgoingLinks:
            yield i


class Link:
    
    def __init__(self, linkID, linkIDEXT, origNodeID_, destNodeID_, linkLen_):
        # internal link id used for sp calculation
        self.id = linkID
        # external link id defined by user or input file
        self.idEXT = linkIDEXT
        self.origNodeID = origNodeID_
        self.destNodeID = destNodeID_
        self.linkLen = linkLen_
    
    def GetOrigNodeID(self):
        return self.origNodeID
    
    def GetDestNodeID(self):
        return self.destNodeID
    
    def GetLen(self):
        return self.linkLen


class SimpleDequePy:
    """ Special implemenation of deque using fix-length array 
    
    the interface utilized for shortest-path algorithms is exactly the same as 
    the built-in deque.
    """
    
    def __init__(self, size_):
        self.nodes = [-1 for i in range(size_)]
        self.head = -1
        self.tail = -1
    
    def __len__(self):
        return self.head != -1
    
    def appendleft(self, nodeID):
        if self.head == -1:
            self.nodes[nodeID] = -1
            self.head = nodeID
            self.tail = nodeID
        else:
            self.nodes[nodeID] = self.head
            self.head = nodeID
    
    def append(self, nodeID):
        if self.head == -1:
            self.head = nodeID
            self.tail = nodeID
            self.nodes[nodeID] = -1
        else:
            self.nodes[self.tail] = nodeID
            self.nodes[nodeID] = -1
            self.tail = nodeID
    
    def popleft(self):
        left = self.head
        self.head = self.nodes[left]
        self.nodes[left] = -1
        return left
    
    def clear(self):
        self.head = -1
        self.tail = -1