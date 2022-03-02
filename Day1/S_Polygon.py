import sympy as sp
points = [[4,10],[9,7],[11,2],[2,2],[4,10]]
result = 0.0
for i in range(len(points) - 1):
    result += 1/2 * abs(sp.Matrix([points[i], points[i+1]]).det())
print(result)