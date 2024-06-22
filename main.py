import numpy as np

def f1(x):
    return (x + np.cos(x))*np.exp(-x**2) + x*np.cos(x)

def f1p(x):
    expTerm = np.exp(-x**2)
    return expTerm - 2*x**2*expTerm - np.sin(x)*expTerm - 2*x*np.cos(x)*expTerm + np.cos(x) - x*np.sin(x)

def newtonsMethod(f, fp, tol, ig):
    err = [1]
    i = 0

    val = ig
    
    while err[i] > tol or i == 0:
        prevVal = val
        val = val - f(val)/fp(val)

        i = i + 1

        err.append(abs(prevVal - val))

    return val
        
    

val = newtonsMethod(f1, f1p, 1e-16, 1.1)
print(val)
