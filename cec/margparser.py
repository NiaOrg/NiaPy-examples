import sys
from NiaPy.util import MakeParser

def MakeArgParserCEC():
	parser = MakeArgParser()
	parser.add_argument('-f', '-fnum', dest='fnum', default=1, type=int)
	return parser

def getArgs(argv):
	parser = makeArgParser()
	args = parser.parse_args(argv)
	return args

def getDictArgs(argv): return vars(getArgs(argv))

if __name__ == '__main__':
	args = getArgs(sys.argv[1:])
	print (args)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
