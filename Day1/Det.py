from itertools import permutations
import numpy as np
import math

def sgn_by_def(sigma, X):
    result = 1.0
    for i in range(len(X) - 1):
        for j in range(i + 1, len(X)):
            result *= (X[i] - X[j]) / (sigma[i] - sigma[j])
    return result

def det_creation(n):
    X = []
    for i in range(1, n+1):
        X.append(i)
    Sn = list(permutations(X))
    det = ""
    for sn in Sn:
        product = ""
        for i in range(1, n+1):
            product = product + "a" + str(i) + str(np.array(sn)[i-1])
        sgn = sgn_by_def(np.array(sn), X)
        if (sgn != 1):
            product = " - " + product
        else:
            product = " + " + product
        det = det + product
    return det
def det_calculation(A):
    X = []
    n = int(math.sqrt(A.size))
    for i in range(1, n+1):
        X.append(i)
    Sn = list(permutations(X))
    det = 0
    for sn in Sn:
        product = 1
        for i in range(1, n+1):
            product = product * A[i-1][sn.index(i)]
        sgn = sgn_by_def(np.array(sn), X)
        if (sgn != 1):
            product = product * (-1)
        det = det + product
    return det

print(det_creation(3))
mtrix = np.array([ [3,5,-8], [4, 12, -1], [2,5,3] ])
print(det_calculation(mtrix))
