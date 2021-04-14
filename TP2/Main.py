from Etudiant import *

etudiant = Etudiant("goulois", "lucas")
etudiant.bulletin.ajouteNote("math", 2)
etudiant.bulletin.ajouteNote("latin", 20)
etudiant.bulletin.ajouteNote("latin", 20)
etudiant.bulletin.ajouteNote("latin", 20)
etudiant.bulletin.ajouteNote("latin", 2)
etudiant.bulletin.ajouteNote("latin", 19)

print(etudiant.bulletin)
print(etudiant.bulletin.moyenneMatiere("latin"))
print(etudiant)
