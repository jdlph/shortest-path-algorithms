"""Implemenations of Modified Label Correcting (MLC) Algorithm for
Single Source Shortest Path Problem (SSSP) including:
    
    1. FIFO
    2. Double-Ended Queue (Deque)
    3. Minimum Distance Label (essentially Dijkstra's Algorithm)

07/19/20, Peiheng Li (jdlph@hotmail.com)
"""


from time import time
import heapq
import collections
import SimpleDequeC
from classes import SimpleDequePy
from utilities import MAX_LABEL, dist_apsp, pred_apsp, \
                      GetNode, GetLink, GetNextNodeID, GetNumNodes


def CalculateSSSPFIFOI(srcNodeID, dist, pred):
    """ FIFO implementation of MLC using built-in list and x in s operation
    
    The time complexity of x in s operation for built-in list is O(n), where n
    is the size of list at run time.
    """
    dist[srcNodeID] = 0
    # list
    selist = []
    selist.append(srcNodeID)
    # label correcting
    while selist:
        i = selist.pop(0)
        pNode = GetNode(i)
        for linkIDX in pNode.GetOutgoingLinks():
            pLink = GetLink(linkIDX)
            j = pLink.GetDestNodeID()
            if dist[j] > dist[i] + pLink.GetLen():
                dist[j] = dist[i] + pLink.GetLen()
                pred[j] = i
                if j not in selist:
                    selist.append(j)


def CalculateSSSPFIFOII(srcNodeID, numNode, dist, pred):
    """ FIFO implementation of MLC using built-in list and indicator array

    x in s operation for built-in list can be replaced using an 
    indicator/status array. The time complexity is only O(1).
    """
    status = [0 for i in range(numNode)]
    dist[srcNodeID] = 0
    # list
    selist = []
    selist.append(srcNodeID)
    status[srcNodeID] = 1
    # label correcting
    while selist:
        i = selist.pop(0)
        status[i] = 0
        pNode = GetNode(i)
        for linkIDX in pNode.GetOutgoingLinks():
            pLink = GetLink(linkIDX)
            j = pLink.GetDestNodeID()
            if dist[j] > dist[i] + pLink.GetLen():
                dist[j] = dist[i] + pLink.GetLen()
                pred[j] = i
                if not status[j]:
                    selist.append(j)
                    status[j] = 1


def CalculateSSSPDEQI(srcNodeID, numNode, dist, pred):
    """ Deque implementation of MLC using list and Dr. Zhou's approach.
    
    The time complexities of pop(0) and insert(0, x) for built-in list are both 
    O(n), where n is the size of list at run time.
    """
    status = [0 for i in range(numNode)]
    dist[srcNodeID] = 0
    # list
    selist = []
    selist.append(srcNodeID)
    status[srcNodeID] = 1
    # label correcting
    while selist:
        i = selist.pop(0)
        # 2 indicates the current node p appeared in selist before 
        # but is no longer in it.
        status[i] = 2
        pNode = GetNode(i)
        for linkIDX in pNode.GetOutgoingLinks():
            pLink = GetLink(linkIDX)
            j = pLink.GetDestNodeID()
            if dist[j] > dist[i] + pLink.GetLen():
                dist[j] = dist[i] + pLink.GetLen()
                pred[j] = i
                if status[j] != 1:
                    if status[j] == 2:
                        selist.insert(0, j)
                    else:
                        selist.append(j)
                    status[j] = 1


def CalculateSSSPDEQII(srcNodeID, numNode, dist, pred):
    """ Deque implementation of MLC using deque and Dr. Zhou's approach.
    
    The computation efficiency can be improve by replacing built-in list with 
    deque as well as the following operations:
        1. popleft(),  
        2. appendleft(x).
    Their running times are both O(1).
    """
    status = [0 for i in range(numNode)]
    dist[srcNodeID] = 0
    # deque, choose one of the following three
    selist = collections.deque()
    # selist = SimpleDequePy(numNode)
    # selist = SimpleDequeC.deque(numNode)
    selist.append(srcNodeID)
    status[srcNodeID] = 1
    # label correcting
    while selist:
        i = selist.popleft()
        # 2 indicates the current node p appeared in selist before 
        # but is no longer in it.
        status[i] = 2
        pNode = GetNode(i)
        for linkIDX in pNode.GetOutgoingLinks():
            pLink = GetLink(linkIDX)
            j = pLink.GetDestNodeID()
            if dist[j] > dist[i] + pLink.GetLen():
                dist[j] = dist[i] + pLink.GetLen()
                pred[j] = i
                if status[j] != 1:
                    if status[j] == 2:
                        selist.appendleft(j)
                    else:
                        selist.append(j)
                    status[j] = 1                      


def CalculateSSSPDijkstraI(srcNodeID, numNode, dist, pred):
    """ Minimum Distance Label Implementation without heap

    There are two major operations with this implementation: 
        1. Find the node with the minimum distance label from the scan eligible
           list by looping through all the nodes in this list, which takes O(n) 
           time;
        2. Remove this node from list by the built-in remove() operation, which 
           takes O(n) time as well.
        
    The overall time complexity of these two operations is O(n), where, n is 
    the list size at run time.
    """
    status = [0 for i in range(numNode)]
    dist[srcNodeID] = 0
    # list
    selist = []
    selist.append(srcNodeID)
    status[srcNodeID] = 1
    # label correcting
    while selist:
        i = GetNextNodeID(selist, dist)
        selist.remove(i)
        status[i] = 0
        pNode = GetNode(i)
        for linkIDX in pNode.GetOutgoingLinks():
            pLink = GetLink(linkIDX)
            j = pLink.GetDestNodeID()
            if dist[j] > dist[i] + pLink.GetLen():
                dist[j] = dist[i] + pLink.GetLen()
                pred[j] = i
                if not status[j]:
                    selist.append(j)
                    status[j] = 1


def CalculateSSSPDijkstraII(srcNodeID, dist, pred):
    """ Minimum Distance Label Implementation using heap 

    heappop(h) from heapq involves two operations:
        1. Find the object with the minimum key from heap h;
        2. Delete the object with the minimum key from heap h.

    As h is a binary heap, the two operations require O(1) time and O(logn) 
    time respectively. The overall time complexity of these two operations is
    O(logn) compared to O(n) in the implementation without heap.
    
    NOTE that this implementation is DIFFERENT with the standard heap 
    implementation of Dijkstra's Algorithm as there is no
    decrease-key(h, newval, i) in heaqp from Python STL to reduce the key of an
    object i from its current value to newval.

    Omitting decrease-key(h, newval, i) WOULD NOT affect the correctness of the
    implementation.
    """
    dist[srcNodeID] = 0
    # heap
    selist = []
    heapq.heapify(selist)
    heapq.heappush(selist, (dist[srcNodeID], srcNodeID))
    # label correcting
    while selist:
        (k, i) = heapq.heappop(selist)
        pNode = GetNode(i)
        for linkIDX in pNode.GetOutgoingLinks():
            pLink = GetLink(linkIDX)
            j = pLink.GetDestNodeID()
            if dist[j] > k + pLink.GetLen():
                dist[j] = k + pLink.GetLen()
                pred[j] = i
                heapq.heappush(selist, (dist[j], j))


def CalculateAPSP(method='dij'):
    """ All Pair Shortest Path (APSP) Algorithms.

    Please choose one of the three implementations: fifo, deq, dij.

    All pair shortest paths can be calculated by: 
        1. repeated Single-Source Shortest Path Algorithms
        2. Floyd-Warshall Algorithm
    """
    st = time()

    # initialization
    numNode = GetNumNodes()
    dist_apsp = [[MAX_LABEL]*numNode for i in range(numNode)]
    pred_apsp = [[-1]*numNode for i in range(numNode)]

    if method.lower().startswith('dij'):
        for i in range(numNode):
            CalculateSSSPDijkstraI(i, numNode, dist_apsp[i], pred_apsp[i])
            # CalculateSSSPDijkstraII(i, dist_apsp[i], pred_apsp[i])
    elif method.lower().startswith('deq'):
        for i in range(numNode):
            CalculateSSSPDEQI(i, numNode, dist_apsp[i], pred_apsp[i])
            #CalculateSSSPDEQII(i, numNode, dist_apsp[i], pred_apsp[i])
    elif method.lower().startswith('fifo'):
        for i in range(numNode):
            CalculateSSSPFIFOI(i, dist_apsp[i], pred_apsp[i])
            # CalculateSSSPFIFOII(i, numNode, dist_apsp[i], pred_apsp[i])
    elif method.lower().startswith('fw'):
        # do nothing
        print("not implemented yet")
    else:
        raise Exception('Please choose correct shortest path algorithm: '
                        +'dij; deq; fifo; fw.')
    
    print('Processing time for SPP\t: {0: .2f}'.format(time() - st)+' s.')