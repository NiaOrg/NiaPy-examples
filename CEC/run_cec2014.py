# encoding=utf8
import sys

sys.path.append('cec2014')

import random
import logging
from numpy import asarray
from NiaPy import Runner
from NiaPy.util import Task, TaskConvPrint, TaskConvPlot, OptimizationType
from cec2014 import run_fun
from cecargparser import getDictArgs

logging.basicConfig()
logger = logging.getLogger('cec_run')
logger.setLevel('INFO')

# For reproducive results
random.seed(1234)

class MinMB(object):
	def __init__(self, fnum=1):
		self.Lower = -100
		self.Upper = 100
		self.fnum = fnum

	def function(self):
		def evaluate(D, sol): return run_fun(asarray(sol), self.fnum)
		return evaluate

class MaxMB(MinMB):
	def function(self):
		f = MinMB.function(self)
		def e(D, sol): return -f(D, sol)
		return e

def simple_example(alg, fnum=1, runs=10, D=10, nFES=50000, nGEN=5000, seed=None, optType=OptimizationType.MINIMIZATION, optFunc=MinMB, **kwu):
	for i in range(runs):
		task = Task(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc(fnum))
		algo = alg(seed=seed, task=task)
		Best = algo.run()
		logger.info('%s %s' % (Best[0], Best[1]))

def logging_example(alg, fnum=1, D=10, nFES=50000, nGEN=5000, seed=None, optType=OptimizationType.MINIMIZATION, optFunc=MinMB, **ukw):
	task = TaskConvPrint(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc(fnum))
	algo = alg(seed=seed, task=task)
	best = algo.run()
	logger.info('%s %s' % (best[0], best[1]))

def plot_example(alg, fnum=1, D=10, nFES=50000, nGEN=5000, seed=None, optType=OptimizationType.MINIMIZATION, optFunc=MinMB, **kwy):
	task = TaskConvPlot(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc(fnum))
	algo = alg(seed=seed, task=task)
	best = algo.run()
	logger.info('%s %s' % (best[0], best[1]))
	input('Press [enter] to continue')

def getOptType(otype):
	if otype == OptimizationType.MINIMIZATION: return MinMB
	elif otype == OptimizationType.MAXIMIZATION: return MaxMB
	else: return None

if __name__ == '__main__':
	pargs = getDictArgs(sys.argv[1:])
	algo = Runner.getAlgorithm(pargs['algo'])
	optFunc = getOptType(pargs['optType'])
	if not pargs['runType']: simple_example(algo, optFunc=optFunc, **pargs)
	elif pargs['runType'] == 'log': logging_example(algo, optFunc=optFunc, **pargs)
	elif pargs['runType'] == 'plot': plot_example(algo, optFunc=optFunc, **pargs)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
