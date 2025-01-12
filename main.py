import exercice1
import exercice2


def menu():
    options = {
        "1": ("Exercice 1", exercice1.main),
        "2": ("Exercice 2", exercice2.main),
        "3": ("Exercice 3", ""),
        "4": ("Exercice 4", ""),
        "q": ("Quitter", None)
    }

    while True:
        print("\n--- Menu ---")
        for key, (description, _) in options.items():
            print(f"{key}: {description}")

        choice = input("\nSélectionnez une option : ").strip()

        if choice in options:
            description, action = options[choice]
            if action:
                print(f"\nExécution de : {description}\n")
                action()
            else:
                print("\nAu revoir !")
                break
        else:
            print("\nOption invalide. Veuillez réessayer.")


if __name__ == "__main__":
    menu()
