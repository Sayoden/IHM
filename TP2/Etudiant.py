from TP2.Bulletin import Bulletin

class Etudiant:
    def __init__(self, nom, prenom):
        self.nom = str(nom)
        self.prenom = str(prenom)
        self.bulletin = Bulletin()

    def __str__(self):
        return self.nom + " " + self.prenom

