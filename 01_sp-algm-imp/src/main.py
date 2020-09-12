"""User interface for Shortest Path Algorithm Implementations

08/05/20, Peiheng Li (jdlph@hotmail.com)
"""


from utilities import ReadLinks
from spalgorithms import CalculateAPSP


def main():
    ReadLinks("C:/dev/spp/data/ShrkLink.txt", '\t')
    CalculateAPSP('dij')


if __name__=='__main__':
    main()