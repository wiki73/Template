from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextOption, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QComboBox, QDialog, QTableWidgetItem, QSizePolicy, \
    QRadioButton, QMessageBox, QPushButton, QLineEdit, QLabel, QVBoxLayout, QWidget
from sql import SQL


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

        # Создаем поле для ввода названия папки
        self.folder_name_input = QLineEdit()
        layout.addWidget(self.folder_name_input)

        # Создаем кнопку 'Создать'
        self.create_button = QPushButton("Создать")
        self.create_button.clicked.connect(self.simulate_create_folder)
        layout.addWidget(self.create_button)

        # Устанавливаем макет для окна
        self.setLayout(layout)

    def simulate_create_folder(self):
        """Имитация создания папки с введенным именем."""
        folder_name = self.folder_name_input.text().strip()
        if folder_name:  # Проверка на пустое имя
            # Здесь мы просто показываем сообщение о "создании" папки
            QMessageBox.information(self, "Успех", f"Папка '{folder_name}' успешно создана (имитация).")
        else:
            QMessageBox.warning(self, "Предупреждение", "Введите название папки.")
class ComboBox(QComboBox):
    def __init__(self):
        super().__init__()
        self.addItems(['Папка 1', 'Новая папка'])
        self.window = None
        self.currentTextChanged.connect(self.text_change)

    def text_change(self):
        if self.currentText() == 'Новая папка':
            self.window = CreateFolderApp()
            self.window.show()

