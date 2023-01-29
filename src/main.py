"""User interface for Shortest Path Algorithm Implementations

08/05/20, Peiheng Li (jdlph@hotmail.com)
"""


from utils import ReadLinks, ReadNodes
from spalgm import CalculateAPSP


def main():
    # make sure your cwd is shortest-path-algorithms
    ReadNodes('data/node_chicago.csv')
    ReadLinks('data/link_chicago.csv')
    CalculateAPSP('deq')


if __name__=='__main__':
    main()