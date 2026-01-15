#creation de classe Outils:

class Outils:
    def __init__(self):
        self.nombres = []

    def saisir(self):
        self.nombres = []
        for i in range(10):
            n = int(input("Entrez un entier : "))
            self.nombres.append(n)

    def min(self):
        minimum = self.nombres[0]
        for n in self.nombres:
            if n < minimum:
                minimum = n
        return minimum

    def max(self):
        maximum = self.nombres[0]
        for n in self.nombres:
            if n > maximum:
                maximum = n
        return maximum

    def somme(self):
        total = 0
        for n in self.nombres:
            total += n
        return total

    def moyenne(self):
        return self.somme() / len(self.nombres)

outil = Outils()
outil.saisir()

print("Le plus petit entier est :", outil.min())
print("Le plus grand entier est :", outil.max())
print("La somme des entiers est :", outil.somme())
print("La moyenne des entiers est :", outil.moyenne())