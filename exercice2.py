
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit

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



window.show()
app.exec()

