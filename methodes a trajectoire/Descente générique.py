# Algorithme: Méthode de descente générique
# Données: f, E,
# Initialisation choix d‘une solution initiale( aléatoire ou avec un heuristique )
# Solution initiale (courante ) x0,
# Solution optimale courante x*=x0, k=1
# Tant que le test d’arrêt non satisfait:
#     1. Génération des voisins candidats : voisinage
#     2. Choix du meilleur voisin candidats xk
#     3. Si f(xk) f(x*) alors x*=xk ,    , k=k+1,  Aller en (1)
#         Fin si
#  Fin Tant que

import random
import math


def descente_generique(f, E, choix_init='aleatoire', max_iter=1000, tol=1e-6):
    """
    Algorithme de descente générique.
    f : fonction objectif à minimiser.
    E : ensemble des solutions réalisables.
    choix_init : méthode de choix de la solution initiale ('aleatoire' ou une fonction heuristique).
    max_iter : nombre maximum d'itérations.
    tol : tolérance pour le critère d'arrêt.
    """
    # Initialisation
    if choix_init == 'aleatoire':
        x0 = random.choice(E)
    else:
        x0 = choix_init(E)
    x_opt = x0
    k = 1

    # Boucle principale
    while k <= max_iter:
        # Génération des voisins candidats
        voisins = voisinage(x_opt, E)

        # Choix du meilleur voisin candidat
        x_k = min(voisins, key=lambda x: f(x))

        # Test d'arrêt
        if f(x_k) < f(x_opt) - tol:
            x_opt = x_k

        k += 1

    return x_opt


def voisinage(x, E):
    """
    Fonction qui retourne tous les voisins de x dans l'ensemble E.
    """
    voisins = []
    for i in range(len(x)):
        for v in E:
            if v[i] != x[i]:
                voisins.append(v)
    return voisins


# Fonction à minimiser
def f(x):
    return x ** 2 + math.sin(x)


# Ensemble des solutions réalisables (ici, un intervalle)
E = [x / 10 for x in range(-100, 101)]


# Méthode heuristique pour le choix de la solution initiale
def choix_init(E):
    return 0.0


# Test de l'algorithme de descente générique
x_opt = descente_generique(f, E, choix_init=choix_init)

print("Solution optimale : x =", x_opt)
print("Valeur minimale de la fonction : f(x) =", f(x_opt))

