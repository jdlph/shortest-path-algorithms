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
# map user-defined node id to internal node id
_map_uid_id = {}


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
            linkUID = r[0].strip()
            origNodeID = GetNodeID(r[1])
            destNodeID = GetNodeID(r[2])
            linkLen = float(r[3])
            pLink = Link(linkID, linkUID, origNodeID, destNodeID, linkLen)
            _dict_links[linkID] = pLink
            # update outgoing links from orig node
            _dict_nodes[origNodeID].AddOutgoingLinks(linkID)
            linkID += 1


def ReadNodes(fileName, delimiter_=','):
    """ read node input file and set up node objects.
    
    This function will automatically create an internal node ID for each node. 
    Internal node IDs are consecutive non-negative integers starting from 0 as 
    required by initializations of dist_apsp and pred_apsp. 
    
    See CalculateAPSP(method='dij') for details.
    """
    global _dict_nodes
    global _map_uid_id

    with open(fileName) as f:
        # skip the header
        next(f)
        csvf = csv.reader(f, delimiter=delimiter_)
        # internal node id used for calculation
        nodeID = 0
        for r in csvf:
            # note that nodeUID here is STRING
            nodeUID = r[0].strip()
            _dict_nodes[nodeID] = Node(nodeID, nodeUID)
            if nodeUID not in _map_uid_id.keys():
                _map_uid_id[nodeUID] = nodeID
            else:
                raise Exception('DUPLICATE NODE ID FOUND: '+nodeUID)
            nodeID += 1


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


def GetNodeID(nodeUID):
    """ get the internal node id given a user-defined node id """
    try:
        return _map_uid_id[nodeUID]
    except KeyError:
        raise Exception('INCONSISTENCY FOUND between LINK and NODE FILES: '
                        +'Node '+str(nodeUID)+' NOT EXIST in NODE FILE!!')


def GetNextNodeID(nodes, dist):
    """ return node ID with the minimum distance label from a set of nodes """
    # empty nodes
    if not nodes:
        raise Exception('Empty Scan Eligible List!!')
    
    nodeID = nodes[0]
    min_ = dist[nodeID]
    for i in nodes:
        if dist[i] < min_:
            min_ = dist[i]
            nodeID = i
    
    return nodeID