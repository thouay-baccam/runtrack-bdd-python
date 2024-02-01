class Employe:
    def __init__(self, base_de_donnees):
        self.base_de_donnees = base_de_donnees

    def lister_grands_salaires(self):
        requete = "SELECT * FROM employe WHERE salaire > 3000"
        employes = self.base_de_donnees.executer_requete(requete)
        for employe in employes:
            print(employe)

    def lister_employes_et_service(self):
        requete = """
        SELECT e.nom, e.prenom, s.nom AS nom_service
        FROM employe e
        INNER JOIN service s ON e.id_service = s.id
        """
        employes = self.base_de_donnees.executer_requete(requete)
        for employe in employes:
            print(employe)
