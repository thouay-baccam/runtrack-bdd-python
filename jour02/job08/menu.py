from zoodatabase import ZooDatabase
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

def modifier_animal(db):
    id_animal = input("Entrez l'ID de l'animal à modifier: ")
    nom = input("Entrez le nouveau nom de l'animal: ")
    espece = input("Entrez la nouvelle espèce de l'animal: ")
    id_cage = input("Entrez le nouvel ID de la cage: ")
    date_naissance = input("Entrez la nouvelle date de naissance (YYYY-MM-DD): ")
    pays_origine = input("Entrez le nouveau pays d'origine: ")
    animal = Animal(nom, espece, id_cage, date_naissance, pays_origine)
    animal.update(db, id_animal)
    print("Animal modifié avec succès.")

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

def modifier_cage(db):
    id_cage = input("Entrez l'ID de la cage à modifier: ")
    superficie = input("Entrez la nouvelle superficie de la cage: ")
    capacite_max = input("Entrez la nouvelle capacité maximale: ")
    cage = Cage(superficie, capacite_max)
    cage.update(db, id_cage)
    print("Cage modifiée avec succès.")

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
        print("2. Modifier un animal")
        print("3. Supprimer un animal")
        print("4. Lister tous les animaux")
        print("5. Ajouter une cage")
        print("6. Modifier une cage")
        print("7. Supprimer une cage")
        print("8. Lister toutes les cages")
        print("9. Quitter")
        choix = input("Choisissez une option: ")

        if choix == '1':
            ajouter_animal(db)
        elif choix == '2':
            modifier_animal(db)
        elif choix == '3':
            supprimer_animal(db)
        elif choix == '4':
            lister_animaux(db)
        elif choix == '5':
            ajouter_cage(db)
        elif choix == '6':
            modifier_cage(db)
        elif choix == '7':
            supprimer_cage(db)
        elif choix == '8':
            lister_cages(db)
        elif choix == '9':
            break
        else:
            print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu()
