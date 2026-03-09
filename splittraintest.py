import numpy as np
X = np.array([1, 2, 3, 4, 5])
Y = np.array([2, 4, 6, 8, 10])
# np.random.seed(42)
np.random.shuffle(X)
np.random.shuffle(Y)
print(X)
print(Y)