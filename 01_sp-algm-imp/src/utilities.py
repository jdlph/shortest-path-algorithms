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
_dict_nodes = {}
# global container to store all link objects
_dict_links = {}
# map external node id to internal node id
_map_ext_int = {}


def ReadLinks(fileName, delimiter_=','):
    """ read link input file and set up link objects.
    
    This function will automatically create an internal link id for each link. 
    Internal link IDs are consecutive non-negative integers starting from 0.
    """
    global _dict_links
    global _dict_nodes
    
    with open(fileName) as f:
        # skip the header
        next(f)
        csvf = csv.reader(f, delimiter=delimiter_)
        # internal link id used for calculation
        linkID = 0
        for r in csvf:
            linkIDEXT = r[0].strip()
            origNodeID = GetInternalNodeID(int(r[1]))
            destNodeID = GetInternalNodeID(int(r[2]))
            linkLen = float(r[3])
            pLink = Link(linkID, linkIDEXT, origNodeID, destNodeID, linkLen)
            _dict_links[linkID] = pLink
            # update outgoing links from orig node
            _dict_nodes[origNodeID].AddOutgoingLinks(linkID)
            linkID += 1
    f.close()


def ReadNodes(fileName, delimiter_=','):
    """ read node input file and set up node objects.
    
    This function will automatically create an internal node ID for each node. 
    Internal node IDs are consecutive non-negative integers starting from 0 as 
    required by initializations of dist_apsp and pred_apsp. 
    
    See CalculateAPSP(method='dij') for details.
    """
    global _dict_nodes
    global _map_ext_int

    with open(fileName) as f:
        # skip the header
        next(f)
        csvf = csv.reader(f, delimiter=delimiter_)
        # internal node id used for calculation
        nodeID = 0
        for r in csvf:
            nodeIDEXT = r[0].strip()
            if nodeID not in _dict_nodes.keys():
                _dict_nodes[nodeID] = Node(nodeID, nodeIDEXT)
            if nodeIDEXT not in _map_ext_int.keys():
                _map_ext_int[nodeIDEXT] = nodeID
            nodeID += 1
    f.close()


def GetNumNodes():
    """ return the number of nodes on the current network """
    return len(_dict_nodes.keys())
    

def GetNode(nodeID):
    """ get the corresponding node object given internal nodeID """
    try:
        return _dict_nodes[nodeID]
    except KeyError:
        return None


def GetLink(linkID):
    """ get the corresponding link object given internal linkID """
    try:
        return _dict_links[linkID]
    except KeyError:
        return None


def GetInternalNodeID(nodeIDEXT):
    """ get the internal node id given an external node id """
    try:
        return _map_ext_int[nodeIDEXT]
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