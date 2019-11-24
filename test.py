import numpy as np 
import matplotlib.pyplot as plt 
from golden import golden 

def f(x):
	return (x**2 - 6.*x + 12.) / (x**2 + 6.*x + 12.)

a = 0.
b = 20.
x = np.linspace(a, b, 200)
y = f(x)

plt.plot(x,y)
plt.xlabel('x')
plt.grid(True)
plt.show()

xMin, fMin = golden(f, a, b)
print("xMin = {}, fMin = {}".format(xMin, fMin))