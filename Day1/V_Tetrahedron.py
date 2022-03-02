import sympy as sp
M = sp.Matrix([[0, 4, 1, 1], [4, 0, 0, 1], [3, 5, 2, 1], [2, 2,5, 1]])
print(abs(1/6*M.det()))