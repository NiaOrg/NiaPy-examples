# encoding=utf8
import sys

import random

import logging
import pandas as pd
from numpy import asarray, savetxt, set_printoptions, inf

from NiaPy.algorithms import AlgorithmUtility
from NiaPy.benchmarks import Benchmark
from NiaPy.task import StoppingTask, OptimizationType
from cecargparser import getDictArgs

logging.basicConfig()
logger = logging.getLogger('cec_run')
logger.setLevel('INFO')

# For reproducive results
random.seed(1234)
# For output results printing
set_printoptions(linewidth=10000000, formatter={'all': lambda x: str(x)})

class MinMB(Benchmark):
	def __init__(self, run_fun, Lower=-100, Upper=100, fnum=1):
		Benchmark.__init__(self, Lower=Lower, Upper=Upper)
		self.fnum = fnum
		self.run_fun = run_fun

	def function(self): return lambda x: self.run_fun(asarray(x), self.fnum)

class MaxMB(MinMB):
	def function(self):
		f = MinMB.function(self)
		return lambda x: -f(x)

cdimsOne = [2, 10, 30, 50]
cdimsTwo = [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
cdimsThree = [10, 30, 50, 100]
cdimsFour = [10, 30]
cdimsFive = [9, 10, 16, 18]

def getCecBench(cec, d):
	if cec == 5:
		sys.path.append('cec2005')
		from cec2005 import run_fun
		if d not in cdimsOne: raise Exception('Dimension sould be in %s' % (cdimsOne))
	elif cec == 8:
		sys.path.append('cec2008')
		from cec2008 import run_fun
	elif cec == 13:
		sys.path.append('cec2013')
		from cec2013 import run_fun
		if d not in cdimsTwo: raise Exception('Dimension sould be in %s' % (cdimsTwo))
	elif cec == 14:
		sys.path.append('cec2014')
		from cec2014 import run_fun
		if d not in cdimsThree: raise Exception('Dimension sould be in %s' % (cdimsThree))
	elif cec == 15:
		sys.path.append('cec2015')
		from cec2015 import run_fun
		if d not in cdimsFour: raise Exception('Dimension sould be in %s' % (cdimsFour))
	elif cec == 16:
		sys.path.append('cec2016')
		from cec2016 import run_fun
		if d not in cdimsOne: raise Exception('Dimension sould be in %s' % (cdimsOne))
	elif cec == 17:
		sys.path.append('cec2017')
		from cec2017 import run_fun
		if d not in cdimsThree: raise Exception('Dimension sould be in %s' % (cdimsThree))
	elif cec == 18:
		sys.path.append('cec2018')
		from cec2018 import run_fun
		if d not in cdimsThree: raise Exception('Dimension sould be in %s' % (cdimsThree))
	elif cec == 19:
		sys.path.append('cec2019')
		from cec2019 import run_fun
		if d not in cdimsFive: raise Exception('Dimension sould be in %s' % (cdimsThree))
	return run_fun

def getMaxFES(cec):
	if cec == 8: return 5000
	elif cec in [5, 13, 14, 15, 17, 18]: return 10000
	elif cec == 19: return inf
	else: return 10000

def simple_example(alg, cec, fnum=1, runs=10, D=10, nFES=50000, nGEN=5000, seed=[None], optType=OptimizationType.MINIMIZATION, optFunc=MinMB, wout=False, sr=[-100, 100], **kwu):
	bests, func = list(), getCecBench(cec, D)
	for i in range(runs):
		task = StoppingTask(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc(func, sr[0], sr[1], fnum))
		algo = alg(seed=seed[i % len(seed)])
		best = algo.run(task)
		logger.info('%s %s' % (best[0], best[1]))
		bests.append(best)
	if wout:
		bpos, bval = asarray([x[0] for x in bests]), asarray([x[1] for x in bests])
		savetxt('%s_%d_%d_p' % (algo.Name[-1], fnum, D), bpos)
		savetxt('%s_%d_%d_v' % (algo.Name[-1], fnum, D), bval)

def logging_example(alg, cec, fnum=1, D=10, nFES=50000, nGEN=5000, seed=[None], optType=OptimizationType.MINIMIZATION, optFunc=MinMB, wout=False, sr=[-8192, 8192], **kwu):
	func = getCecBench(cec, D)
	task = StoppingTask(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc(func, sr[0], sr[1], fnum), logger=True)
	algo = alg(seed=seed[0], NP=100, vMin=-16000, vMax=16000, w=0.5)
	best = algo.run(task)
	logger.info('%s %s' % (best[0], best[1]))

def save_example(alg, cec, fnum=1, runs=10, D=10, nFES=50000, nGEN=5000, seed=[None], optType=OptimizationType.MINIMIZATION, optFunc=MinMB, wout=True, sr=[-100, 100], **kwu):
	bests, conv_it, conv_f, func = list(), list(), list(), getCecBench(cec, D)
	for i in range(runs):
		task = StoppingTask(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc(func, sr[0], sr[1], fnum))
		algo = alg(seed=seed[i % len(seed)])
		best = algo.run(task)
		logger.info('%s %s' % (best[0], best[1]))
		bests.append(best)
		conv_it.append(task.evals)
		conv_f.append(task.x_f_vals)
	if wout:
		bpos, bval = asarray([x[0] for x in bests]), asarray([x[1] for x in bests])
		savetxt('%s_%d_%d_p' % (algo.Name[-1], fnum, D), bpos)
		savetxt('%s_%d_%d_v' % (algo.Name[-1], fnum, D), bval)
		inds = []
		for i in range(runs): inds.append('evals'), inds.append('funvl')
		data = []
		for i in range(runs): data.append(conv_it[i]), data.append(conv_f[i])
		pd.DataFrame(data, index=inds).T.to_csv('%s_%d_%d.csv' % (algo.Name[-1], fnum, D), sep=',', index=False)

def plot_example(alg, cec, fnum=1, D=10, nFES=50000, nGEN=5000, seed=[None], optType=OptimizationType.MINIMIZATION, optFunc=MinMB, wout=False, sr=[-100, 100], **kwu):
	func = getCecBench(cec, D)
	task = TaskConvPlot(D=D, nFES=nFES, nGEN=nGEN, optType=optType, benchmark=optFunc(func, sr[0], sr[1], fnum))
	algo = alg(seed=seed[0])
	best = algo.run(task)
	logger.info('%s %s' % (best[0], best[1]))
	input('Press [enter] to continue')

def getOptType(otype):
	if otype == OptimizationType.MINIMIZATION: return MinMB
	elif otype == OptimizationType.MAXIMIZATION: return MaxMB
	else: return None

if __name__ == '__main__':
	pargs = getDictArgs(sys.argv[1:])
	fes = getMaxFES(pargs['cec']) if not inf else sys.maxsize
	pargs['nFES'] = round(pargs['D'] * fes * pargs['reduc'])
	algUtl = AlgorithmUtility()
	algo = algUtl.get_algorithm(pargs['algo'])
	optFunc = getOptType(pargs['optType'])
	if not pargs['runType']: simple_example(algo, optFunc=optFunc, **pargs)
	elif pargs['runType'] == 'log': logging_example(algo, optFunc=optFunc, **pargs)
	elif pargs['runType'] == 'plot': plot_example(algo, optFunc=optFunc, **pargs)
	elif pargs['runType'] == 'save': save_example(algo, optFunc=optFunc, **pargs)
	else: simple_example(algo, optFunc=optFunc, **pargs)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
