from parse_acc import parse_data
import sys


if __name__ == '__main__':
    dados = parse_data(filter_sigma = sys.argv[2],filter_m_movel = sys.argv[3], file_name = sys.argv[4])
    dados.plot(sys.argv[1])