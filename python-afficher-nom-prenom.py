class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

p = Personne("Laurent","Alexis", 30)

print("Votre nom : " + p.nom + " | ", "Votre prenom : " + p.prenom + " | ", "Votre age : " + str(p.age))
