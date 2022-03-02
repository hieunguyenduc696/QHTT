from sympy import *
# Hãy viết phương trình mặt phẳng đi qua 3 điểm (-1, 3, 2), (0, 1, 0), (-2, 0, 1).
# PT MP di qua 3 diem la dinh thuc:
# | x  y z 1 |
# | -1 3 2 1 |
# | 0  1 0 1 |
# | -2 0 1 1 |
x, y, z = symbols('x y z')
MP = Matrix([[x, y, z, 1],[-1, 3, 2, 1],[0, 1, 0, 1],[-2, 0,1, 1]])
print(MP.det())