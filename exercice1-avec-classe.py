# creation de classe triangle

class Triangle:
    def __init__(self, n):
        self.n = n

    # creation du premier triangle
    def ligne_inversee(self, i):
        return ' ' * (self.n - i) + '*' * i

    # ligne du deuxième triangle (normal)
    def ligne_normale(self, i):
        return '*' * i

# Classe Affichage : s'occupe uniquement d'afficher les triangles
class Affichage:
    def __init__(self, triangle):
        self.triangle = triangle

    def afficher(self):
        for i in range(1, self.triangle.n + 1):
            print(self.triangle.ligne_inversee(i) + ' ' + self.triangle.ligne_normale(i))

