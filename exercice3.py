from utils import getData
import seaborn as sns
import matplotlib.pyplot as plt

def main():
    # Récupération des données nettoyées via la fonction getData()
    df_cleaned = getData()

    # Sélection des colonnes nécessaires pour l'analyse
    df_2022 = df_cleaned[['écrans', 'fauteuils', 'entrées 2022']]

    # Calcul des corrélations entre les colonnes sélectionnées
    # Corrélation entre le nombre d'écrans et les entrées 2022
    corr_ecrans_entrees = df_2022['écrans'].corr(df_2022['entrées 2022'])

    # Corrélation entre le nombre de fauteuils et les entrées 2022
    corr_fauteuils_entrees = df_2022['fauteuils'].corr(df_2022['entrées 2022'])

    # Affichage des résultats des corrélations
    print(f"Corrélation entre le nombre d'écrans et les entrées 2022 : {corr_ecrans_entrees}")
    print(f"Corrélation entre le nombre de fauteuils et les entrées 2022 : {corr_fauteuils_entrees}")

    # Visualisation de la relation entre le nombre d'écrans et les entrées 2022
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x='écrans',
        y='entrées 2022',
        data=df_2022,
        scatter_kws={'s': 20},
        line_kws={'color': 'red'}
    )
    plt.title('Relation entre le nombre d\'écrans et les entrées 2022')
    plt.xlabel('Nombre d\'écrans')
    plt.ylabel('Entrées annuelles 2022')
    plt.tight_layout()
    plt.savefig('exercice3-ecran.png')
    plt.close()
    print("Le graphique vient d'être sauvegardé dans le fichier 'exercice3-ecran.png'")

    # Visualisation de la relation entre le nombre de fauteuils et les entrées 2022
    plt.figure(figsize=(10, 6))
    sns.regplot(
        x='fauteuils',
        y='entrées 2022',
        data=df_2022,
        scatter_kws={'s': 20},
        line_kws={'color': 'red'}
    )
    plt.title('Relation entre le nombre de fauteuils et les entrées 2022')
    plt.xlabel('Nombre de fauteuils')
    plt.ylabel('Entrées annuelles 2022')
    plt.tight_layout()
    plt.savefig('exercice3-fauteuils.png')
    plt.close()
    print("Le graphique vient d'être sauvegardé dans le fichier 'exercice3-fauteuils.png'")
