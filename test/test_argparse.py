import argparse

parser = argparse.ArgumentParser(description='Metrics definition database operations')
parser.add_argument('-o', '--operation', dest="operation", type=str, required=True, help='{...}')
parser.add_argument('-n', '--name', dest="name", type=str, required=True, help='{...}')

args = parser.parse_args()
print (args)
