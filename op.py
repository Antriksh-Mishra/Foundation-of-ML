# import numpy as np

# A = np.array([[1, 2],
#               [3, 4]])
# a=np.array([10,20,30])
# B = np.array([[5, 6],
#               [7, 8]])
# # print(np.dot(A,B))
# # print(A.T)
# # print(A.shape)
# print(np.random.randint(1,6,size=5))
# print(np.random.choice(a))
# print(np.random.seed()
# )

import numpy as np

# np.random.seed(60)
# print(np.random.randint(8))
# seed give the same random values or fixes the values in random
# np.random.seed(10)
# print(np.random.rand(3))

a = np.array([[1, 2, 3],
              [4, 5, 6]])
c=np.array([1,2,3,5,5,6])
# shuffle changes int he original array
# np.random.shuffle(a)
# permutation creates a copy 
b=np.random.permutation(a)
print(b)
np.random.seed(c)
print(np.random.permutation(len( c)))

