import sympy as sp
# 4 diem nam trong 1 mp khong gian 3 chieu thi V = 0
M = sp.Matrix([[0, 4, 1, 1], [4, 0, 0, 1], [3, 5, 2, 1], [2, 2,5, 1]])
V = abs(1/6*M.det())
if (V == 0):
    print("yes")
else:
    print("no")