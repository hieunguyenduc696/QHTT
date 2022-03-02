import numpy as np
n = 4
X = np.array(range(1, n+1))
sigma = np.array([2,1,3,4])

def sgn_by_def(sigma):
    result = 1.0
    for i in range(len(X) - 1):
        for j in range(i + 1, len(X)):
            result *= (X[i] - X[j]) / (sigma[i] - sigma[j])
    return result

print(sgn_by_def(sigma))