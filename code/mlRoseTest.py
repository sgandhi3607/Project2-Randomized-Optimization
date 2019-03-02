import mlrose
import numpy as np

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import accuracy_score


# # Initialize fitness function object using pre-defined class
# fitness = mlrose.Queens()
#
# # Define optimization problem object
# problem = mlrose.DiscreteOpt(length = 8, fitness_fn = fitness, maximize=False, max_val=8)
#
# # Define decay schedule
# schedule = mlrose.ExpDecay()
#
#
# # Solve using simulated annealing - attempt 1
# np.random.seed(1)
#
# init_state = np.array([0, 1, 2, 3, 4, 5, 6, 7])
# best_state, best_fitness = mlrose.simulated_annealing(problem, schedule = schedule, max_attempts = 10,
#                                                       max_iters = 1000, init_state = init_state)
#
# print(best_state)
#
# print(best_fitness)




# Load the Iris dataset
data = load_iris()
