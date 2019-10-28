import sys
from NiaPy.util import MakeArgParser

ccecs = [8, 13, 14, 15, 16, 17, 18, 19]
creduces = [0.01, 0.02, 0.03, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

def positiveInt(x): return abs(int(x))

def str2bool(x): return True if x in ['true', 'True', 'TRUE', 'T', 'yes', 'Yes', 'YES', 'Y'] else False

def MakeArgParserCEC():
	parser = MakeArgParser()
	parser.add_argument('-c', '--cec', dest='cec', default=ccecs[-1], choices=ccecs, type=int)
	parser.add_argument('-f', '--fnum', dest='fnum', default=1, type=positiveInt)
	parser.add_argument('-sr', '--srange', dest='srange', nargs=2, default=[-100, 100], type=int)
	parser.add_argument('-d', '--dim', dest='D', default=10, type=positiveInt)
	parser.add_argument('-nr', '--nFESreduc', dest='reduc', default=creduces[-1], choices=creduces, type=float)
	parser.add_argument('-rn', '--rnum', dest='runs', default=51, type=positiveInt)
	parser.add_argument('-o', '--wout', dest='wout', default=True, type=str2bool)
	return parser

def getArgs(argv):
	parser = MakeArgParserCEC()
	args = parser.parse_args(argv)
	return args

def getDictArgs(argv): return vars(getArgs(argv))

if __name__ == '__main__':
	args = getArgs(sys.argv[1:])
	print (args)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
