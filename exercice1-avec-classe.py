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

