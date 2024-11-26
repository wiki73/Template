import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QMenu, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Контекстное меню в PyQt6")

        # Создаем центральный виджет
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Создаем контекстное меню
        self.context_menu = QMenu(self)

        # Добавляем действия в контекстное меню
        action1 = QAction("Действие 1", self)
        action2 = QAction("Действие 2", self)
        action3 = QAction("Действие 3", self)

        self.context_menu.addAction(action1)
        self.context_menu.addAction(action2)
        self.context_menu.addAction(action3)

        # Устанавливаем стиль для контекстного меню
        self.context_menu.setStyleSheet("""
            QMenu {
                background-color: red;
                border: 1px solid #a0a0a0;
            }
            QMenu::item {
                padding: 8px 16px;
            }
            QMenu::item:selected {
                background-color: #a0a0a0;
                color: white;
            }
        """)

        # Подключаем контекстное меню к событию правой кнопки мыши
        self.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)

    def contextMenuEvent(self, event):
        self.context_menu.exec(event.globalPos())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
