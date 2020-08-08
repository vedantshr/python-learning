import matplotlib.pyplot as a
import numpy as np

x= (np.random.randint(0,10,100))
a.plot(x, 'b*')
a.ylabel('some numbers')
a.show()