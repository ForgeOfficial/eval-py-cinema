from utils import getData
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


def main():
    df_cleaned = getData()
    X = df_cleaned[['écrans', 'fauteuils', 'population de la commune']]
    y = df_cleaned['entrées 2022']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    print(f"Coefficient de détermination (R²) : {r2}")
    print(f"Erreur moyenne absolue (MAE) : {mae}")

    y_pred_2022 = model.predict(X)

    df_cleaned['entrées prédites 2022'] = y_pred_2022

    print("\nComparaison des entrées réelles et prédites pour 2022:")
    print(
        df_cleaned[['écrans', 'fauteuils', 'population de la commune', 'entrées 2022', 'entrées prédites 2022']].head())
