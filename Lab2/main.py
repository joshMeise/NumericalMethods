import numpy as np

def f1(x):
    return (x + np.cos(x))*np.exp(-x**2) + x*np.cos(x)

def f1p(x):
    expTerm = np.exp(-x**2)
    return expTerm - 2*x**2*expTerm - 2*x*expTerm*np.cos(x) - expTerm*np.sin(x) + np.cos(x) - x*np.sin(x)

def newtonsMethod(f, fp, tol, ig):
    prevVal = ig
    
    val = prevVal - f(prevVal)/fp(prevVal);
    
    err = np.array([abs(prevVal - val)])

    while err[-1] > tol:
        prevVal = val
        val = prevVal - f(prevVal)/fp(prevVal);
        error = abs(prevVal - val)
        err = np.append(err, error)

    return val

def secantMethod(f, tol, ig1, ig2):
    prevVal1 = ig1
    prevVal2 = ig2

    val = prevVal1 - f(prevVal1)*(prevVal1 - prevVal2)/(f(prevVal1) - f(prevVal2))

    err = np.array([abs(prevVal1 - val)])

    while err[-1] > tol:
        prevVal2 = prevVal1
        prevVal1 = val
        val = prevVal1 - f(prevVal1)*(prevVal1 - prevVal2)/(f(prevVal1) - f(prevVal2))
        error = abs(prevVal1 - val)
        err = np.append(err, error)

    return val
        



print(newtonsMethod(f1, f1p, 1e-16, 1.1))
print(secantMethod(f1, 1e-16, 1.1, 1.5))


