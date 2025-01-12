import pandas as pd


def getData():
    # Chargement du fichier CSV contenant les données des cinémas
    df = pd.read_csv('data/cinemas.csv', delimiter=';', encoding='utf-8')

    # Sélection des colonnes qui nous intéressent pour l'analyse
    columns_of_interest = ['commune', 'écrans', 'fauteuils', 'entrées 2022', 'entrées 2021', 'population de la commune']
    df_filtered = df[columns_of_interest]

    # Suppression des lignes contenant des valeurs manquantes (NaN)
    df_cleaned = df_filtered.dropna()

    return df_cleaned
