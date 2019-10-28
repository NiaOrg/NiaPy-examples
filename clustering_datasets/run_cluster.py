# encoding=utf8
from typing import Union, List, Tuple
import sys
import json

import random
import logging

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, make_blobs
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from NiaPy import Runner
from NiaPy.algorithms import Algorithm
from NiaPy.util import OptimizationType, TaskConvSave, groupdatabylabel, classifie, clusters2labels
from NiaPy.benchmarks import Clustering, ClusteringMin, ClusteringMinPenalty, ClusteringClassification

from clusterargparser import getDictArgs

logging.basicConfig()
logger = logging.getLogger('cec_run')
logger.setLevel('INFO')

def save_example(alg: Algorithm, runs: int = 10, nFES: int = 1000, nGEN: int = np.inf, seed: List[int] = [None], optType: OptimizationType = OptimizationType.MINIMIZATION, dataset: str = 'iris', ofun: str = 'gc', sseed: int = 1, split: float = .3, wout: bool = True, **kwu: dict) -> None:
	data, labels, noc = None, None, 4
	if dataset == 'iris': data, labels = load_iris(True); noc = len(np.unique(labels))
	elif dataset == 'cancer': data, labels = load_breast_cancer(True); noc = len(np.unique(labels))
	elif dataset == 'wine': data, labels = load_wine(True); noc = len(np.unique(labels))
	elif dataset == 'glass': df = pd.read_csv('glass.csv'); data, labels = df.iloc[:, :-1].values, df.iloc[:, -1].values; noc = len(np.unique(labels))
	elif dataset == 'cmc': df = pd.read_csv('cmc.csv'); data, labels = df.iloc[:, :-1].values, df.iloc[:, -1].values; noc = len(np.unique(labels))
	else: data, labels = make_blobs(n_samples=500, n_features=9, centers=noc, random_state=sseed)
	Xt, Xv, yt, yv = train_test_split(data, labels, test_size=split, random_state=sseed)
	lt = LabelEncoder().fit(labels); gl = groupdatabylabel(data, labels, lt)
	bests, conv_it, conv_f, func = list(), list(), list(), None
	if ofun == 'c': func = Clustering(Xt)
	elif ofun == 'cm': func = ClusteringMin(Xt)
	elif ofun == 'cmp': func = ClusteringMinPenalty(Xt)
	elif ofun == 'cc': func = ClusteringClassification(Xt, yt)
	else: sys.exit(2)
	if seed == [None]: seed = list(range(1, runs + 1))
	for it in range(runs):
		task = TaskConvSave(D=noc * len(data[0]), nFES=nFES, nGEN=nGEN, optType=optType, benchmark=func)
		algo = alg(seed=seed[it % len(seed)])
		best = algo.run(task)
		V = best[0].reshape([noc, len(data[0])])
		l, ok = clusters2labels(V, gl), 0
		for i, d in enumerate(Xv): ok += 1 if lt.inverse_transform([l[classifie(d, V)]])[0] == yv[i] else 0
		a = ok / len(Xv)
		logger.info('%d. run:\n%s %s' % (it, V, a))
		bests.append((best[0], a))
		conv_it.append(task.evals)
		conv_f.append(task.x_f_vals)
	if wout:
		with open('%s_%s_%s_args' % (algo.Name[-1], ofun, dataset), 'w') as file: file.write(json.dumps(algo.getParameters()))
		bpos, bval = np.asarray([x[0] for x in bests]), np.asarray([x[1] for x in bests])
		np.savetxt('%s_%s_%s_p' % (algo.Name[-1], ofun, dataset), bpos)
		np.savetxt('%s_%s_%s_v' % (algo.Name[-1], ofun, dataset), bval)
		inds = []
		for i in range(runs): inds.append('evals'), inds.append('funvl')
		data = []
		for i in range(runs): data.append(conv_it[i]), data.append(conv_f[i])
		pd.DataFrame(data, index=inds).T.to_csv('%s_%s_%s.csv' % (algo.Name[-1], ofun, dataset), sep=',', index=False)

if __name__ == '__main__':
	pargs = getDictArgs(sys.argv[1:])
	algo = Runner.getAlgorithm(pargs['algo'])
	save_example(algo, **pargs)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
