import numpy as np

def f(x):
    return (x[0]-2)**2 + (x[1]-3)**2 + 4

def recherche_tabou(f, x0, max_iter=100, tenure=10):
    x = x0
    fx = f(x)
    tabou = [x]
    it = 0
    while it < max_iter:
        it += 1
        x_best = None
        fx_best = np.inf
        for i in range(len(x)):
            for j in range(-1, 2):
                if j == 0:
                    continue
                x_new = np.copy(x)
                x_new[i] += j
                fx_new = f(x_new)
                if fx_new < fx_best and x_new.tolist() not in tabou:
                    x_best = x_new
                    fx_best = fx_new
        if x_best is None:
            break
        x = x_best
        fx = fx_best
        tabou.append(x)
        if len(tabou) > tenure:
            tabou.pop(0)
    return x, fx

# exemple d'utilisation
x0 = np.array([0, 0])
x_min, f_min = recherche_tabou(f, x0)
print("minimum de f trouvé:", f_min)
print("x qui minimise f:", x_min)
