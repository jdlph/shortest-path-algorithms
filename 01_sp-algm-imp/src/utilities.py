"""All Utilities needed for Shortest Path Algorithm Implementations

07/20/20, Peiheng Li (jdlph@hotmail.com)
"""


import csv
from classes import Link, Node


# maximum or infinite number used to initialize distance labels
MAX_LABEL = 9999
# distance labels for APSP
dist_apsp = []
# predecessors for APSP
pred_apsp = []
# global container to store all node objects
dict_nodes = {}
# global container to store all link objects
dict_links = {}


def ReadLinks(fileName, delimiter_=','):
    """ This function is NOT genetic. more specifically, it assumes that node 
    IDs are consecutive non-negative numbers starting from 0 as required by
    initializations of dist_apsp and pred_apsp. 
    
    See CalculateAPSP(method='dij') for details.
    """
    global dict_links
    global dict_nodes

    with open(fileName) as f:
        # skip the header
        # next(f)
        csvf = csv.reader(f, delimiter=delimiter_)
        for r in csvf:
            linkID = int(r[0])
            origNodeID = int(r[1])
            destNodeID = int(r[2])
            linkLen = int(r[3])
            pLink = Link(linkID, origNodeID, destNodeID, linkLen)
            dict_links[linkID] = pLink
            # create node object and store it
            if origNodeID not in dict_nodes.keys():
                dict_nodes[origNodeID] = Node(origNodeID)
            # update outgoing links from orig node
            dict_nodes[origNodeID].AddOutgoingLinks(linkID)
            # create node object and store it
            if destNodeID not in dict_nodes.keys():
                dict_nodes[destNodeID] = Node(destNodeID)
    f.close()


def ReadNodes(fileName, sep=','):
    """ this function is not necessary unless you have attributes other than 
    ID and outgoing links that you want to be enclosed in a Node object.
    """


def GetNumNodes():
    """ return the number of nodes on the current network """
    return len(dict_nodes.keys())
    

def GetNode(nodeID):
    """ get the corresponding node object given nodeID """
    try:
        return dict_nodes[nodeID]
    except KeyError:
        return None


def GetLink(linkID):
    """ get the corresponding link object given linkID """
    try:
        return dict_links[linkID]
    except KeyError:
        return None


def GetNextNodeID(nodes, dist):
    """ return node ID with the minimum distance label from a set of nodes
    
    NOTE that Negative Distance Label is NOT SUPPORTED in this application.
    """
    min_ = MAX_LABEL
    minNodeID = -1
    for i in nodes:
        if dist[i] < min_:
            min_ = dist[i]
            minNodeID = i
    return minNodeID