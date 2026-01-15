
# demander à l'utilisateur de'entrer l'entier
n = int(input("Entrez un entier : "))

# creation des triangles:
for i in range(1, n + 1):
    # premier triangle inversé
    ligne1 = ' ' * (n - i) + '*' * i
