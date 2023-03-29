import random

def recherche_locale(x_init, max_iterations):
    # Initialisation
    x = x_init
    cout_x = f(x)
    iteration = 0

    # Boucle de recherche locale
    while iteration < max_iterations:
        # Génération d'une nouvelle solution voisine
        x_prime = voisin(x)
        cout_x_prime = f(x_prime)

        # Acceptation de la nouvelle solution si elle est meilleure
        if cout_x_prime < cout_x:
            x = x_prime
            cout_x = cout_x_prime

        iteration += 1

    return x



#La fonction f(x) définit la fonction objectif f(x) = x^2 - 6x + 8 que nous cherchons à minimiser.
def f(x):
    return x ** 2 - 6 * x + 8


#La fonction voisin(x) génère une nouvelle solution voisine en ajoutant ou soustrayant un nombre
# aléatoire à la solution courante.
def voisin(x):
    return x + random.uniform(-1, 1)


# Exemple d'utilisation de la fonction de recherche locale
x_init = 5.0
max_iterations = 1000
solution_optimale = recherche_locale(x_init, max_iterations)

print("Solution optimale trouvée: ", solution_optimale)
print("Cout de la solution optimale: ", f(solution_optimale))
