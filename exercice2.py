
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QPushButton

def calculer_double():
    if nombre_input.text() == "":
        valeur = 0
    else:
        valeur = int(nombre_input.text())

    double_valeur = valeur * 2  # ✅ ligne corrigée : on utilise une variable différente pour le calcul
    resultat.setText(str(double_valeur))
    print("valeur double : " + str(valeur))

#creation de la fonction sauvegarde:
def sauvegarder():
    f = open("resultats.txt", "w")
    f.write(resultat.text())
    f.close()

#creation de la fonction charger():
def charger():
    f = open("resultats.txt", "r")
    valeur = f.readline()
    f.close()
    resultat.setText(valeur)

# créer l'application:
app = QApplication([])
window = QWidget()
window.setWindowTitle("tk")
window.resize(400, 200)

#creer le Layout et attacher a la fenetre:
grid = QGridLayout(window)
window.setLayout(grid)

#creer LineEdit
nombre_input = QLineEdit(window)
grid.addWidget(nombre_input, 1, 1)
grid.addWidget(QLabel("Voici le double: "), 2, 0)
#Qlabel:
grid.addWidget(QLabel("Enter la valeur de N: "), 1, 0)
grid.addWidget(QLabel("Voici le double: "), 2, 0)

#Creation QlineEdit de resultat:
resultat = QLineEdit()
grid.addWidget(resultat, 2, 1)

#creation des button:
btn1 = QPushButton("valider l'operation")
grid.addWidget(btn1, 3, 1)
# connecter le button a la fonction:
btn1.clicked.connect(calculer_double)

# Button sauvegarder:
btn_sauver = QPushButton("Sauvegarder")
grid.addWidget(btn_sauver, 4, 0)
btn_sauver.clicked.connect(sauvegarder)

# Button charger:
btn_charger = QPushButton("Charger")
grid.addWidget(btn_charger, 4, 1)
btn_charger.clicked.connect(charger)
f = open("resultats.txt", "w")

window.show()
app.exec()

