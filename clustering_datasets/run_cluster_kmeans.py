# encoding=utf8
from typing import Union, List, Tuple
import logging
import sys

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris, load_wine, load_breast_cancer, make_blobs
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.cluster import KMeans

from NiaPy.util import classifie, clusters2labels, groupdatabylabel

from clusterargparser import getDictArgs

logging.basicConfig()
logger = logging.getLogger('cec_run')
logger.setLevel('INFO')

def save_example(runs: int = 10, nFES: int = 1000, seed: List[int] = [None], dataset: str = 'iris', ofun: str = 'gc', sseed: int = 1, split: float = .3, wout: bool = True, **kwu: dict) -> None:
	data, labels, noc = None, None, 4
	if dataset == 'iris': data, labels = load_iris(True); noc = len(np.unique(labels))
	elif dataset == 'cancer': data, labels = load_breast_cancer(True); noc = len(np.unique(labels))
	elif dataset == 'wine': data, labels = load_wine(True); noc = len(np.unique(labels))
	elif dataset == 'glass': df = pd.read_csv('glass.csv'); data, labels = df.iloc[:, :-1].values, df.iloc[:, -1].values; noc = len(np.unique(labels))
	elif dataset == 'cmc': df = pd.read_csv('cmc.csv'); data, labels = df.iloc[:, :-1].values, df.iloc[:, -1].values; noc = len(np.unique(labels))
	else: data, labels = make_blobs(n_samples=500, n_features=9, centers=noc, random_state=sseed)
	Xt, Xv, yt, yv = train_test_split(data, labels, test_size=split, random_state=sseed)
	lt = LabelEncoder().fit(labels); gl, bests = groupdatabylabel(data, labels, lt), []
	if seed == [None]: seed = list(range(1, runs + 1))
	for it in range(runs):
		kmeans = KMeans(n_clusters=noc, init='random', n_init=100, max_iter=nFES, random_state=1, algorithm='full').fit(Xt)
		C, lt = kmeans.cluster_centers_, LabelEncoder().fit(labels)
		l, ok = clusters2labels(C, groupdatabylabel(Xt, yt, lt)), 0
		for i, d in enumerate(Xv): ok += 1 if lt.inverse_transform([l[classifie(d, C)]]) == yv[i] else 0
		logger.info('%d. run:\n%s %s' % (it, C, ok / len(Xv)))
		bests.append([C.flatten(), ok / len(Xv)])
	if wout:
		bpos, bval = np.asarray([x[0] for x in bests]), np.asarray([x[1] for x in bests])
		np.savetxt('KM_%s_%s_p' % (ofun, dataset), bpos)
		np.savetxt('KM_%s_%s_v' % (ofun, dataset), bval)

if __name__ == '__main__':
	pargs = getDictArgs(sys.argv[1:])
	save_example(**pargs)

# vim: tabstop=3 noexpandtab shiftwidth=3 softtabstop=3
