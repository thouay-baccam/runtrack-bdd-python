# menu.py
from zoo_database import ZooDatabase
from animal import Animal
from cage import Cage

def ajouter_animal(db):
    nom = input("Entrez le nom de l'animal: ")
    espece = input("Entrez l'espèce de l'animal: ")
    id_cage = input("Entrez l'ID de la cage: ")
    date_naissance = input("Entrez la date de naissance (YYYY-MM-DD): ")
    pays_origine = input("Entrez le pays d'origine: ")
    animal = Animal(nom, espece, id_cage, date_naissance, pays_origine)
    animal.save(db)
    print("Animal ajouté avec succès.")

def supprimer_animal(db):
    id_animal = input("Entrez l'ID de l'animal à supprimer: ")
    Animal.delete(db, id_animal)
    print("Animal supprimé avec succès.")

def lister_animaux(db):
    animaux = Animal.get_all(db)
    print("Animaux dans le zoo:")
    for animal in animaux:
        print(animal)

def ajouter_cage(db):
    taille = input("Entrez la taille de la cage: ")
    capacite_max = input("Entrez la capacité maximale: ")
    cage = Cage(taille, capacite_max)
    cage.save(db)
    print("Cage ajoutée avec succès.")

def supprimer_cage(db):
    id_cage = input("Entrez l'ID de la cage à supprimer: ")
    Cage.delete(db, id_cage)
    print("Cage supprimée avec succès.")

def lister_cages(db):
    cages = Cage.get_all(db)
    print("Cages dans le zoo:")
    for cage in cages:
        print(cage)

def menu():
    db = ZooDatabase('localhost', 'zoo', 'root', 'Teddy2212!')

    while True:
        print("\n--- Menu de Gestion du Zoo ---")
        print("1. Ajouter un animal")
        print("2. Supprimer un animal")
        print("3. Lister tous les animaux")
        print("4. Ajouter une cage")
        print("5. Supprimer une cage")
        print("6. Lister toutes les cages")
        print("7. Quitter")
        choix = input("Choisissez une option: ")

        if choix == '1':
            ajouter_animal(db)
        elif choix == '2':
            supprimer_animal(db)
        elif choix == '3':
            lister_animaux(db)
        elif choix == '4':
            ajouter_cage(db)
        elif choix == '5':
            supprimer_cage(db)
        elif choix == '6':
            lister_cages(db)
        elif choix == '7':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
