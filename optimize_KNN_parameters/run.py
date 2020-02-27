import numpy as np
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import cross_validate
from NiaPy.algorithms.modified import HybridBatAlgorithm
import pygal 

KNN_WEIGHT_FUNCTIONS = [
    'uniform',
    'distance'
]

KNN_ALGORITHMS = [
    'ball_tree',
    'kd_tree',
    'brute'
]

# map from real number [0, 1] to integer ranging [5, 15]
def swap_n_neighbors(val):
    return int(val * 10 + 5)

# map from real number [0, 1] to integer ranging [0, 1]
def swap_weights(val):
    if val > 0.5:
        return 1
    return 0

# map from real number [0, 1] to integer ranging [1, 3]
def swap_algorithm(val):
    if val == 1:
        return 3
    return int(val * 3 + 1)

# map from real number [0, 1] to integer ranging [10, 50]
def swap_leaf_size(val):
    return int(val * 10 + 40)

class KNNBreastCancerBenchmark(object):
    def __init__(self):
        self.Lower = 0
        self.Upper = 1
    
    def function(self):
        # our definition of fitness function
        def evaluate(D, solution):
            n_neighbors = swap_n_neighbors(solution[0])
            weights = KNN_WEIGHT_FUNCTIONS[(swap_weights(solution[1]) - 1)]
            algorithm = KNN_ALGORITHMS[(swap_algorithm(solution[2]) - 1)]
            leaf_size = swap_leaf_size(solution[3])

            fitness = 1 - KNNBreastCancerClassifier(1234).evaluate(n_neighbors, weights, algorithm, leaf_size)
            scores.append([fitness, n_neighbors, weights, algorithm, leaf_size])

            return fitness
        return evaluate

class KNNBreastCancerClassifier(object):
    def __init__(self, seed=1234):
        self.seed = seed
        self.ten_fold_scores = {}
        self.default_ten_fold_scores = {}
        np.random.seed(self.seed)

        dataset = datasets.load_breast_cancer()
        self.X = dataset.data
        self.y = dataset.target
        
        self.X_search, self.X_validate, self.y_search, self.y_validate = train_test_split(self.X, self.y, test_size=0.8, random_state=self.seed)
        self.X_search_train, self.X_search_test, self.y_search_train, self.y_search_test = train_test_split(self.X_search, self.y_search, test_size=0.8, random_state=self.seed)


    def evaluate(self, n_neighbors, weights, algorithm, leaf_size):
        model = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights, algorithm=algorithm, leaf_size=leaf_size)
        model.fit(self.X_search_train, self.y_search_train)
        return model.score(self.X_search_test, self.y_search_test)

    def run_10_fold(self, solution=None):
        if solution is None:
            estimator = KNeighborsClassifier()
            kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=self.seed)
            self.default_ten_fold_scores = cross_validate(estimator, self.X, self.y, cv=kfold, scoring=['accuracy'])
        else:
            estimator = KNeighborsClassifier(n_neighbors=solution[1], weights=solution[2], algorithm=solution[3], leaf_size=solution[4])
            kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=self.seed)
            self.ten_fold_scores = cross_validate(estimator, self.X_validate, self.y_validate, cv=kfold, scoring=['accuracy'])


scores = []
algorithm = HybridBatAlgorithm(4, 40, 100, 0.9, 0.1, 0.001, 0.9, 0.0, 2.0, KNNBreastCancerBenchmark())
best = algorithm.run()

print('Optimal KNN parameters are:')
best_solution = []

for score in scores:
    if score[0] == best:
        best_solution = score

print(best_solution)

model = KNNBreastCancerClassifier()
model.run_10_fold(solution=best_solution)
model.run_10_fold()

print('best model mean test accuracy: ' + str(np.mean(model.ten_fold_scores['test_accuracy'])))
print('default model mean test accuracy: ' + str(np.mean(model.default_ten_fold_scores['test_accuracy'])))

box_plot = pygal.Box(width=800, height=600, range=(0.8, 0.99))
box_plot.zero = 0.9
box_plot.title = '10-fold cross-validation accuracies'
box_plot.add('Best model', model.ten_fold_scores['test_accuracy'])
box_plot.add('Default model', model.default_ten_fold_scores['test_accuracy'])

box_plot.render_to_png('chart.png')