from utils import getData


def main():
    # Get data du csv
    df_cleaned = getData()
    # Affiche les 5 premières lignes pour vérifier que tout est correct
    print(df_cleaned.head())

    # Affiche des statistiques descriptives sur les colonnes numériques
    print(df_cleaned.describe())
