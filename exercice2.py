
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QLabel, QPushButton

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

#creation des button:
btn1 = QPushButton("valider l'operation")
grid.addWidget(btn1, 3, 1)



window.show()
app.exec()

