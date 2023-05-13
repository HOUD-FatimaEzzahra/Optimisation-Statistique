import random

# Définir la fonction d'adaptation (fitness) pour évaluer la performance de chaque individu
def fitness(individual):
    # Cette fonction calcule la somme des éléments de l'individu, mais vous pouvez remplacer cela par n'importe quelle fonction d'adaptation qui convient à votre problème.
    return sum(individual)

# Définir la fonction de sélection des parents
def select_parents(population):
    # On peut utiliser n'importe quelle méthode de sélection, mais ici on utilise la roulette wheel selection.
    # Cette méthode sélectionne les parents en fonction de leur score de fitness relatif à la population entière.
    fitness_scores = [fitness(individual) for individual in population]
    total_fitness = sum(fitness_scores)
    selection_probs = [score / total_fitness for score in fitness_scores]
    parent1, parent2 = random.choices(population, weights=selection_probs, k=2)
    return parent1, parent2

# Définir la fonction de croisement (crossover)
def crossover(parent1, parent2):
    # On peut utiliser n'importe quelle méthode de croisement, mais ici on utilise le one-point crossover.
    # Cette méthode sélectionne un point de croisement aléatoire et échange les parties de chaque parent de chaque côté de ce point pour créer deux enfants.
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Définir la fonction de mutation
def mutate(individual, mutation_rate):
    # On peut utiliser n'importe quelle méthode de mutation, mais ici on utilise la mutation par inversion.
    # Cette méthode sélectionne deux points de mutation aléatoires et inverse les éléments entre ces points.
    if random.random() < mutation_rate:
        mutation_point1, mutation_point2 = random.sample(range(len(individual)), 2)
        if mutation_point1 > mutation_point2:
            mutation_point1, mutation_point2 = mutation_point2, mutation_point1
        individual[mutation_point1:mutation_point2+1] = reversed(individual[mutation_point1:mutation_point2+1])

# Définir la fonction principale de l'algorithme génétique
def genetic_algorithm(population_size, individual_size, mutation_rate, generations):
    # Générer une population aléatoire initiale.
    population = [[random.randint(0, 1) for _ in range(individual_size)] for _ in range(population_size)]

    for generation in range(generations):
        # Sélectionner les parents.
        parent1, parent2 = select_parents(population)

        # Croiser les parents pour créer des enfants.
        child1, child2 = crossover(parent1, parent2)

        # Muter les enfants avec une certaine probabilité.
        mutate(child1, mutation_rate)
        mutate(child2, mutation_rate)

        # Remplacer les deux individus les moins performants de la population par les deux enfants.
        fitness_scores = [(fitness(individual), individual) for individual in population]
        fitness_scores.sort()
        population[-2] = child1
        population[-1] = child2

        # Afficher les informations sur la génération actuelle.
        best_individual = max(population, key=fitness)
        print(f"Génération {generation}: meilleure performance = {fitness(best_individual)}")

        # Retourner le meilleur individu trouvé.
        return best_individual
