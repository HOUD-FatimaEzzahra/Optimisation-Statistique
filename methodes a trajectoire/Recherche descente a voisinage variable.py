import numpy as np


#La fonction f est une fonction à deux variables qui retourne la valeur de
#la fonction à minimiser en un point donné x.
def f(x):
    return (x[0]-5)**2 + (x[1]-6)**2 + 8


def descente_voisinage_variable(f, x0, max_iter=1000, alpha=0.1, tol=1e-6):
    x = x0
    fx = f(x)
    it = 0
    while it < max_iter:
        it += 1
        for i in range(len(x)):
            x_new = np.copy(x)
            x_new[i] += alpha
            fx_new = f(x_new)
            if fx_new < fx:
                x = x_new
                fx = fx_new
                break
        alpha /= 2
        if alpha < tol:
            break
    return x, fx



# exemple d'utilisation

x0 = np.array([1, 2])
x_min, f_min = descente_voisinage_variable(f, x0, max_iter=1000, alpha=0.5, tol=1e-8)
print("minimum de f trouvé:", f_min)
print("x qui minimise f:", x_min)
