import argparse


parser = argparse.ArgumentParser(description='test')


parser.add_argument('--n1', type=str)
parser.add_argument('--n2', type=str)

args = parser.parse_args()

print('hello')
print(args.n1)
print(args.n2)