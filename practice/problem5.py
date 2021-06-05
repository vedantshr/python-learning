import numpy as ny
x = ny.array([[0,0], [1,1], [2,2]])
print(x)
print(ny.insert(x, 2, 4))
print(ny.insert(x, 2, 4, axis=1))


