"""User interface for Shortest Path Algorithm Implementations

08/05/20, Peiheng Li (jdlph@hotmail.com)
"""


from utilities import ReadLinks, ReadNodes
from spalgm import CalculateAPSP


def main():
    ReadNodes('01_sp-algm-imp/data/node_chicago.csv')
    ReadLinks('01_sp-algm-imp/data/link_chicago.csv')
    CalculateAPSP('deq')


if __name__=='__main__':
    main()