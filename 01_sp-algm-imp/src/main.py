"""User interface for Shortest Path Algorithm Implementations

08/05/20, Peiheng Li (jdlph@hotmail.com)
"""


from utilities import ReadLinks
from spalgm import CalculateAPSP


def main():
    ReadLinks('01_sp-algm-imp/data/link.csv')
    CalculateAPSP('dij')


if __name__=='__main__':
    main()