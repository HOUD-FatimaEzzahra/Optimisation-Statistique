import random


def recherche_locale(f, E):
    # Générer une solution initiale x0 dans E
    x0 = random.choice(E)
    x_best = x0

    i = 1
    while True:
        # Générer une solution dans le voisinage de x
        x = random.choice(N(x_best))

        # Mettre à jour la solution
        if f(x) < f(x_best):
            x_best = x
            i += 1
        else:
            # STOP si le critère d'arrêt est satisfait
            break

    return x_best


# Exemple d'utilisation
def f(x):
    # Fonction à minimiser
    return x ** 2


def N(x):
    # Voisinage de x : x-1, x+1
    return [x - 1, x + 1]


E = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
x_min = recherche_locale(f, E)
print("Minimum trouvé :", x_min, "f(", x_min, ") =", f(x_min))
