import numpy as np
from itertools import permutations

g = np.array([[7, 5, 8], [3, 13, 9], [5, 8, 2]])
t = 20

for p in permutations(g.flatten()):
    g_ = np.array(p).reshape(g.shape)
    if (g_.sum(axis=0) == t).all():
        print('\n'.join(['\t'.join(map(str, r)) for r in g_.tolist()]))
        break
