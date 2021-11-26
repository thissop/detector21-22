import numpy as np
import matplotlib.pyplot as plt

plt.style.use('ggplot')

def a(t): 
    return 1.37023*(t-20)+8.36*(10**-4)*(t-20)**2

def b(t): 
    return 109+t

def ec_eq(t): 
    ec = 0.889*10**(a(t)/b(t)) 
    return ec

x = np.linspace(0, 50, 100)
y = np.array([ec_eq(i) for i in x])
print(x,y)
plt.plot(x,y)
plt.show()