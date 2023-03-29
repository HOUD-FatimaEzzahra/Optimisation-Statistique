import numpy as np

def f(x):
    return (x[0]-2)**2 + (x[1]-3)**2 + 4

def recherche_locale_guidee(f, x0, max_iter=100, alpha=0.1, beta=0.5, gamma=2, tol=1e-6):
    x = x0
    fx = f(x)
    it = 0
    while it < max_iter:
        it += 1
        x_best = x
        fx_best = fx
        for i in range(len(x)):
            x_new = np.copy(x)
            x_new[i] += alpha
            fx_new = f(x_new)
            if fx_new < fx_best:
                x_best = x_new
                fx_best = fx_new
            else:
                x_new[i] -= 2 * alpha
                fx_new = f(x_new)
                if fx_new < fx_best:
                    x_best = x_new
                    fx_best = fx_new
                else:
                    x_new[i] += alpha
            x = x_best
            fx = fx_best
            alpha *= beta
            if alpha < tol:
                break
    return x, fx

# exemple d'utilisation
x0 = np.array([0, 0])
x_min, f_min = recherche_locale_guidee(f, x0)
print("minimum de f trouvé:", f_min)
print("x qui minimise f:", x_min)
