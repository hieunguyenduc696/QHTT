# 1/2 * det
# S = 1/2 * det
import sympy as sp
TG = sp.Matrix([[1,0,1],[4,3,1],[2,2,1]])
print(1/2 * TG.det())