
from PyQt6.QtWidgets import QApplication, QWidget

# créer l'application:
app = QApplication([])
window = QWidget()
window.setWindowTitle("tk")
window.resize(300, 200)  # optionnel, sinon fenêtre très petite

window.show()
app.exec()

