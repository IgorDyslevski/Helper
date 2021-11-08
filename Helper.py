import webbrowser
from PyQt6.QtWidgets import QInputDialog, QWidget, QApplication
import sys


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        while True:
            text, ok = QInputDialog.getText(self, 'Input', 'Enter your problem (English):')
            if ok:
                webbrowser.open(f'https://google.gik-team.com/?q={text.replace(" ", "+")}')
            else:
                exit(0)


apl = QApplication(sys.argv)
app = App()
app.show()
sys.exit(apl.exec())
