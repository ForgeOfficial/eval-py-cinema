from utils import getData
import matplotlib.pyplot as plt


def main():
    # Récupération des données nettoyées via la fonction getData()
    df_cleaned = getData()

    # Calcul du nombre d'entrées par fauteuil pour chaque commune
    # On ajoute une nouvelle colonne au DataFrame
    df_cleaned['entrées par fauteuil'] = (
            df_cleaned['entrées 2022'] / df_cleaned['fauteuils']
    )

    # Calcul de la moyenne des entrées par fauteuil par commune
    df_region_avg = (
        df_cleaned.groupby('commune')['entrées par fauteuil'].mean().reset_index()
    )

    # Sélection des 3 meilleures communes (selon les entrées par fauteuil)
    top_3_commune = df_region_avg.nlargest(3, 'entrées par fauteuil')

    # Sélection des 3 pires communes (selon les entrées par fauteuil)
    bottom_3_commune = df_region_avg.nsmallest(3, 'entrées par fauteuil')

    # Affichage des résultats pour les meilleures communes
    print("Top 3 communes avec les meilleurs résultats en termes d'entrées moyennes par fauteuil :")
    print(top_3_commune)

    # Affichage des résultats pour les pires communes
    print("\nTop 3 communes avec les pires résultats en termes d'entrées moyennes par fauteuil :")
    print(bottom_3_commune)

    # Sélection des 10 meilleures communes ou moins si le DataFrame est plus petit
    top_commune = df_region_avg.nlargest(min(10, len(df_region_avg)), 'entrées par fauteuil')

    # Calcul du nombre de communes pour ajuster la largeur du graphique
    num_commune = len(top_commune)

    # Ajustement des dimensions du graphique
    fig_width = max(10, num_commune * 2)  # Largeur du graphique
    fig_height = 6  # Hauteur fixe

    # Création du graphique en barres
    plt.figure(figsize=(fig_width, fig_height))
    plt.bar(range(num_commune), top_commune['entrées par fauteuil'], color='skyblue')

    # Ajout des labels et du titre
    plt.xlabel('Commune')
    plt.ylabel('Entrées moyennes par fauteuil')
    plt.title('Top 10 des communes avec les entrées moyennes par fauteuil en 2022')
    plt.xticks(range(num_commune), top_commune['commune'], rotation=45, ha='right')  # Rotation des noms pour lisibilité
    plt.tight_layout()  # Optimisation des espaces dans le graphique

    # Sauvegarde du graphique dans un fichier image
    plt.savefig('exercice2.png')
    plt.close()

    # Message pour indiquer que le graphique a été sauvegardé
    print("Le graphique vient d'être sauvegardé dans le fichier 'exercice2.png'")
