# encoding=utf8
import sys

import numpy as np

from NiaPy.util import MakeArgParser

datasets = ['iris', 'cancer', 'wine', 'glass', 'cmc', 'gen']
optfuncs = ['c', 'cm', 'cmp', 'cc']

def positiveInt(x: str) -> int: return abs(int(x))

def prob(x: str) -> float: return float(x) if 0 < float(x) < 1 else np.random.rand()

def str2bool(x: str) -> bool: return True if x in ['true', 'True', 'TRUE', 'T', 'yes', 'Yes', 'YES', 'Y'] else False

def MakeArgParserClustering():
	parser = MakeArgParser()
	parser.add_argument('-ds', '--dataset', dest='dataset', default=datasets[0], choices=datasets, type=str)
	parser.add_argument('-of', '--optfunc', dest='ofun', default=optfuncs[-1], choices=optfuncs, type=str)
	parser.add_argument('-rn', '--rnum', dest='runs', default=51, type=positiveInt)
	parser.add_argument('-ss', '--sseed', dest='sseed', default=1, type=positiveInt)
	parser.add_argument('-sp', '--split', dest='split', default=.3, type=prob)
	parser.add_argument('-o', '--wout', dest='wout', default=True, type=str2bool)
	return parser

def getArgs(argv):
	parser = MakeArgParserClustering()
	args = parser.parse_args(argv)
	return args

def getDictArgs(argv): return vars(getArgs(argv))

if __name__ == '__main__':
	args = getArgs(sys.argv[1:])
	print (args)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
