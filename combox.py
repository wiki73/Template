from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextOption, QColor, QAction
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QDialog, QTableWidgetItem, QSizePolicy, \
    QRadioButton, QMessageBox, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget, QMenu
from sql import SQL

SQL = SQL()


class CreateFolderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Создать новую папку")
        self.setFixedSize(300, 150)  # Устанавливаем фиксированный размер окна

        # Создаем вертикальный макет
        layout = QVBoxLayout()
        # Создаем метку
        self.label = QLabel("Введите название папки:")
        layout.addWidget(self.label)

        self.folder_name_input = QLineEdit()
        layout.addWidget(self.folder_name_input)

        self.create_button = QPushButton("Создать")
        self.create_button.clicked.connect(self.simulate_create_folder)
        layout.addWidget(self.create_button)

        self.setLayout(layout)

    def add_folder(self):
        print(1)
        SQL.insert_folder(self.folder_name_input.text())
        print(2)

    def simulate_create_folder(self):
        self.add_folder()
        folder_name = self.folder_name_input.text().strip()
        if folder_name:
            QMessageBox.information(self, "Успех", f"Папка '{folder_name}' успешно создана (имитация).")
        else:
            QMessageBox.warning(self, "Предупреждение", "Введите название папки.")


class ComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.fuling_combobox()
        self.window = None
        self.currentTextChanged.connect(self.text_change)

    def contextMenuEvent(self, event):
        menu = QMenu(self)

        action1 = menu.addAction("Удалить папку")

        action = menu.exec(event.globalPos())
        if action == action1:
            print("Выбрано действие 1")
            reply = QMessageBox.question(self, 'Подтверждение', "Вы уверены, что хотите ужадить папку?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)

            if reply == QMessageBox.StandardButton.Yes:
                SQL.delete_by_name_folder(self.currentText())
            else:
                print('нет')

    def text_change(self):
        if self.currentText() == 'Новая папка':
            self.window = CreateFolderApp()
            self.window.show()

    def fuling_combobox(self):
        self.clear()
        for i in SQL.get_all_folder():
            self.addItem(i[0])
        self.addItem('Новая папка')
