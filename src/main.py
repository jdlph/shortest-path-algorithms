"""User interface for Shortest Path Algorithm Implementations

08/05/20, Peiheng Li (jdlph@hotmail.com)
"""


from utilities import ReadLinks, ReadNodes
from spalgm import CalculateAPSP


def main():
    # make sure your cwd is shortest-path-problem
    ReadNodes('data/node_chicago.csv')
    ReadLinks('data/link_chicago.csv')
    CalculateAPSP('dij')


if __name__=='__main__':
    main()