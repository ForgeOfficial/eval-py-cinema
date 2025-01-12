# CinemaDataAnalysis

Ce projet est une analyse des données cinématographiques en France, réalisée pour le ministère de la Culture. L'objectif principal est d'évaluer l'impact des infrastructures cinématographiques (nombre d'écrans et fauteuils) sur les entrées annuelles, et de construire un modèle prédictif pour estimer les entrées futures.

---

## Objectifs du projet

1. **Exploration des données** :
    - Nettoyer et comprendre le dataset.
    - Explorer les tendances liées aux entrées annuelles.

2. **Analyse statistique** :
    - Identifier les corrélations entre les infrastructures et la fréquentation.
    - Visualiser ces relations avec des graphiques clairs.

3. **Modélisation prédictive** :
    - Construire un modèle de régression linéaire pour prédire les entrées annuelles.

4. **Recommandations stratégiques** :
    - Proposer des stratégies pour améliorer les entrées en fonction des infrastructures.

---

## Détails techniques

### Données utilisées
Le dataset "cinemas.csv" contient les informations importante suivantes :
- **commune** : Nom de la commune.
- **ecrans** : Nombre d'écrans.
- **fauteuils** : Nombre total de fauteuils.
- **entrées 2021** : Année (2021).
- **entrées 2022** : Année (2022).

### Bibliothèques utilisées
- **Pandas** : Manipulation et exploration des données.
- **Matplotlib & Seaborn** : Visualisations.
- **Scikit-learn** : Modélisation prédictive.

---

## Comment exécuter le projet
1. Clonez ce repository :
   ```bash
   git clone <lien_du_repository>
   ```
2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
3. Lancer le main.py :
   ```bash
   python main.py
   ```

---

## Réponses aux questions

### Exercice 3 : Variable ayant le plus d'impact
La corrélation entre le nombre d'écrans et les entrées annuelles est plus forte, ce qui en fait le facteur le plus influent comparé au nombre de fauteuils.

### Exercice 4 : Performances du modèle
Le nombre d'écrans et de fauteuils influence les entrées, mais d'autres facteurs comme la localisation et la programmation des films sont également essentiels. Ces variables seules ne suffisent pas à prédire avec précision les entrées annuelles.

### Exercice 5 : Recommandations stratégiques
En fonction de la situation du cinéma, il serait stratégique de commencer par augmenter le nombre de fauteuils de 20 %, car cela semble directement lié à une augmentation significative des entrées. Si le cinéma dispose de suffisamment d'espace et de ressources, l'ajout d'écrans pourrait également être envisagé pour maximiser l'impact sur les entrées.

---

## Auteur
Maxime
