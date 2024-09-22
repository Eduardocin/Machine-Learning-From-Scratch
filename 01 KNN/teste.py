import numpy as np
from collections import Counter


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

data_teste = np.array([2, 3, 4, 5 , 5, 6 ,7])

print(data_teste)

x_teste = (2, 4, 4, 3, 5, 6, 7 )

most_common = Counter(data_teste).most_common(1)[0][0]

print(most_common)