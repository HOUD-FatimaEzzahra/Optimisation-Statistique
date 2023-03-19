import random
import math

# Données du problème
villes = ["Casablanca", "Rabat", "Tanger", "Fès", "Marrakech"]
distances = [[0, 87, 331, 293, 235],
             [87, 0, 238, 186, 328],
             [331, 238, 0, 310, 678],
             [293, 186, 310, 0, 506],
             [235, 328, 678, 506, 0]]

# Paramètres de l'algorithme
temperature = 10000
temperature_min = 1
alpha = 0.99
iterations_par_temperature = 100

# Fonction pour calculer la distance totale d'un itinéraire
def calculer_distance(itineraire):
    distance_totale = 0
    for i in range(len(itineraire)-1):
        ville_actuelle = itineraire[i]
        ville_suivante = itineraire[i+1]
        distance_totale += distances[ville_actuelle][ville_suivante]
    distance_totale += distances[itineraire[-1]][itineraire[0]]
    return distance_totale

# Algorithme de recuit simulé
itineraire_actuel = list(range(len(villes)))
meilleur_itineraire = list(range(len(villes)))
random.shuffle(itineraire_actuel)
meilleur_distance = calculer_distance(itineraire_actuel)
while temperature > temperature_min:
    for i in range(iterations_par_temperature):
        # Générer un itinéraire voisin en permutant deux villes
        voisin = itineraire_actuel.copy()
        i = random.randint(0, len(villes)-1)
        j = random.randint(0, len(villes)-1)
        voisin[i], voisin[j] = voisin[j], voisin[i]
        # Calculer la différence de distance entre l'itinéraire voisin et l'itinéraire actuel
        delta_distance = calculer_distance(voisin) - calculer_distance(itineraire_actuel)
        # Accepter l'itinéraire voisin si il est meilleur ou avec une certaine probabilité si il est moins bon
        if delta_distance < 0 or math.exp(-delta_distance/temperature) > random.random():
            itineraire_actuel = voisin.copy()
            distance_actuelle = calculer_distance(itineraire_actuel)
            if distance_actuelle < meilleur_distance:
                meilleur_itineraire = itineraire_actuel.copy()
                meilleur_distance = distance_actuelle
    temperature *= alpha

# Afficher le résultat
print("Meilleur itinéraire trouvé : ")
for i in meilleur_itineraire:
    print(villes[i])
print("Distance totale parcourue : ", meilleur_distance)
