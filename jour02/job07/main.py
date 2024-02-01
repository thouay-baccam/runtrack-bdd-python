from lethaldatabase import LethalDatabase
from employe import Employe

def main():
    # Créer une instance de la base de données
    database = LethalDatabase("localhost", "root", "Teddy2212!", "lethalcompany")

    # Créer une instance d'Employe
    employe = Employe(database)

    # Effectuer les opérations
    print("Employé avec un salaire supérieur à 3000:")
    employe.lister_grands_salaires()

    print("\nEmployés et leur service:")
    employe.lister_employes_et_service()

if __name__ == "__main__":
    main()
