# encoding=utf8
import sys
import logging
import numpy as np
from niapy.problems import Problem
from niapy.task import Task, OptimizationType
from niapy.util.factory import get_algorithm
from cecargparser import make_argparser_cec

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


dims_one = [2, 10, 30, 50]
dims_two = [2, 5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
dims_three = [10, 30, 50, 100]
dims_four = [10, 30]


def get_cec_functions(cec, d):
    if cec == 5:
        sys.path.append('cec2005')
        from cec2005 import run_fun
        if d not in dims_one:
            raise RuntimeError('Dimension should be in %s' % dims_one)
    elif cec == 8:
        sys.path.append('cec2008')
        from cec2008 import run_fun
    elif cec == 13:
        sys.path.append('cec2013')
        from cec2013 import run_fun
        if d not in dims_two:
            raise RuntimeError('Dimension should be in %s' % dims_two)
    elif cec == 14:
        sys.path.append('cec2014')
        from cec2014 import run_fun
        if d not in dims_three:
            raise RuntimeError('Dimension should be in %s' % dims_three)
    elif cec == 15:
        sys.path.append('cec2015')
        from cec2015 import run_fun
        if d not in dims_four:
            raise RuntimeError('Dimension should be in %s' % dims_four)
    elif cec == 16:
        sys.path.append('cec2016')
        from cec2016 import run_fun
        if d not in dims_one:
            raise RuntimeError('Dimension should be in %s' % dims_one)
    elif cec == 17:
        sys.path.append('cec2017')
        from cec2017 import run_fun
        if d not in dims_three:
            raise RuntimeError('Dimension should be in %s' % dims_three)
    elif cec == 18:
        sys.path.append('cec2018')
        from cec2018 import run_fun
        if d not in dims_three:
            raise RuntimeError('Dimension should be in %s' % dims_three)
    elif cec == 19:
        sys.path.append('cec2019')
        from cec2019 import run_fun
        if d not in dims_three:
            raise RuntimeError('Dimension should be in %s' % dims_three)
    return run_fun


def get_max_evals(cec):
    if cec == 8:
        return 5000
    else:
        return 10000


def run_cec(alg, cec, fnum=1, dimension=10, max_evals=50000, opt_type=OptimizationType.MINIMIZATION, wout=False, sr=(-100, 100), run_type='', runs=10, **_kwargs):
    func = get_cec_functions(cec, dimension)
    problem = MinMB(func, dimension, sr[0], sr[1], fnum)

    if not run_type:
        best_coords = []
        best_fitnesses = []
        for _ in range(runs):
            task = Task(problem, optimization_type=opt_type, max_evals=max_evals)
            best_x, best_fit = alg.run(task)
            logger.info('%s %s' % (best_x, best_fit))
            best_coords.append(best_x)
            best_fitnesses.append(best_fit)

        if wout:
            np.savetxt('{}_{}_{}_p'.format(
                alg.Name[1], fnum, dimension), np.asarray(best_coords))
            np.savetxt('{}_{}_{}_v'.format(
                alg.Name[1], fnum, dimension), np.asarray(best_fitnesses))
    elif run_type == 'log':
        task = Task(problem, optimization_type=opt_type,
                    max_evals=max_evals, enable_logging=True)
        best_x, best_fit = alg.run(task)
        logger.info('%s %s' % (best_x, best_fit))
    else:
        task = Task(problem, optimization_type=opt_type, max_evals=max_evals)
        best_x, best_fit = alg.run(task)
        logger.info('%s %s' % (best_x, best_fit))
        task.plot()


if __name__ == '__main__':
    parser = make_argparser_cec()
    args = parser.parse_args()
    args['max_evals'] = round(
        args['dimension'] * get_max_evals(args['cec']) * args['reduc'])
    algo = get_algorithm(args['algo'], seed=args['seed'][0])
    run_cec(algo, **args)
