import numpy as np

def f(x):
    return (x[0]-2)**2 + (x[1]-3)**2 + 4

def recherche_recuit_simule(f, x0, T=100, alpha=0.95, min_T=1e-6):
    x = x0
    fx = f(x)
    T_init = T
    while T > min_T:
        x_new = np.copy(x)
        i = np.random.randint(0, len(x))
        x_new[i] += np.random.normal(0, T)
        fx_new = f(x_new)
        df = fx_new - fx
        if df < 0 or np.exp(-df/T) > np.random.rand():
            x = x_new
            fx = fx_new
        T *= alpha
    return x, fx

# exemple d'utilisation
x0 = np.array([0, 0])
x_min, f_min = recherche_recuit_simule(f, x0)
print("minimum de f trouvé:", f_min)
print("x qui minimise f:", x_min)
