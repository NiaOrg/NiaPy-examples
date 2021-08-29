# encoding=utf8
import sys
import logging
import numpy as np
from niapy.problems import Problem
from niapy.task import Task, OptimizationType
from niapy.util.factory import get_algorithm
from cecargparser import getDictArgs

logging.basicConfig()
logger = logging.getLogger('cec_run')
logger.setLevel('INFO')

# For output results printing
np.set_printoptions(linewidth=10000000, formatter={'all': lambda x: str(x)})


class MinMB(Problem):
    def __init__(self, run_fun, dimension, lower=-100, upper=100, fnum=1):
        super().__init__(dimension, lower, upper)
        self.fnum = fnum
        self.run_fun = run_fun

    def _evaluate(self, x):
        return self.run_fun(x, self.fnum)


cdimsOne = [2, 10, 30, 50]
cdimsTwo = [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
cdimsThree = [10, 30, 50, 100]
cdimsFour = [10, 30]


def getCecBench(cec, d):
    if cec == 5:
        sys.path.append('cec2005')
        from cec2005 import run_fun
        if d not in cdimsOne:
            raise RuntimeError('Dimension sould be in %s' % (cdimsOne))
    elif cec == 8:
        sys.path.append('cec2008')
        from cec2008 import run_fun
    elif cec == 13:
        sys.path.append('cec2013')
        from cec2013 import run_fun
        if d not in cdimsTwo:
            raise RuntimeError('Dimension sould be in %s' % (cdimsTwo))
    elif cec == 14:
        sys.path.append('cec2014')
        from cec2014 import run_fun
        if d not in cdimsThree:
            raise RuntimeError('Dimension sould be in %s' % (cdimsThree))
    elif cec == 15:
        sys.path.append('cec2015')
        from cec2015 import run_fun
        if d not in cdimsFour:
            raise RuntimeError('Dimension sould be in %s' % (cdimsFour))
    elif cec == 16:
        sys.path.append('cec2016')
        from cec2016 import run_fun
        if d not in cdimsOne:
            raise RuntimeError('Dimension sould be in %s' % (cdimsOne))
    elif cec == 17:
        sys.path.append('cec2017')
        from cec2017 import run_fun
        if d not in cdimsThree:
            raise RuntimeError('Dimension sould be in %s' % (cdimsThree))
    elif cec == 18:
        sys.path.append('cec2018')
        from cec2018 import run_fun
        if d not in cdimsThree:
            raise RuntimeError('Dimension sould be in %s' % (cdimsThree))
    elif cec == 19:
        sys.path.append('cec2019')
        from cec2019 import run_fun
        if d not in cdimsThree:
            raise RuntimeError('Dimension sould be in %s' % (cdimsThree))
    return run_fun


def getMaxFES(cec):
    if cec == 8:
        return 5000
    else:
        return 10000


def run_cec(alg, cec, fnum=1, dimension=10, max_evals=50000, opt_type=OptimizationType.MINIMIZATION, wout=False, sr=(-100, 100), run_type='', runs=10, **kwargs):
    func = getCecBench(cec, dimension)
    problem = MinMB(func, dimension, sr[0], sr[1], fnum)
    task = Task(problem, optimization_type=opt_type,
                max_evals=max_evals, enable_logging=run_type == 'log')

    if not run_type:
        best_coords = []
        best_fitnesses = []
        for _ in runs:
            best_x, best_fit = alg.run(task)
            logger.info('%s %s' % (best_x, best_fit))
            best_coords.append(best_x)
            best_fitnesses.append(best_fit)

        if wout:
            np.savetxt('{}_{}_{}_p'.format(
                alg.Name[1], fnum, dimension), np.asarray(best_coords))
            np.savetxt('{}_{}_{}_v'.format(
                alg.Name[1], fnum, dimension), np.asarray(best_fitnesses))
    else:
        best_x, best_fit = alg.run(task)
        logger.info('%s %s' % (best_x, best_fit))

    if run_type == 'plot':
        task.plot()


if __name__ == '__main__':
    pargs = getDictArgs(sys.argv[1:])
    pargs['max_evals'] = round(
        pargs['dimension'] * getMaxFES(pargs['cec']) * pargs['reduc'])
    algo = get_algorithm(pargs['algo'], seed=pargs['seed'][0])
    run_cec(algo, **pargs)


# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
