import sqlite3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QTextOption, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QSizePolicy, \
    QRadioButton
from desinger_file.ui_file import Ui_MainWindow
from second_window import SecondWindow
from sql import SQL
from table_widget import Table



class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initui()
        self.current_check_button = 'Всё'
        self.form_frame()
        self.second_window = None
        self.setWindowTitle('Template')

    def initui(self):
        self.table = Table()
        self.SQL = SQL()
        self.verticalLayout_2.addWidget(self.table)
        self.horizontalSlider.setMinimum(5)  # Минимальный размер шрифта
        self.horizontalSlider.setMaximum(25)  # Максимальный размер шрифта
        self.horizontalSlider.setValue(10)  # Устанавливаем первоначальный размер шрифта

        self.Add_s.clicked.connect(self.add_s)  # добавить шаблон
        self.update_table_bnt.clicked.connect(self.update_table)  # обновить табилицу
        self.check_button_group.buttonClicked.connect(self.check_btn_group)  # Фильтр по tag
        self.table.itemClicked.connect(self.on_item_click)  # добавление кода
        self.clear_button.clicked.connect(self.clear_btn)  # отчистить
        self.copy_code_button.clicked.connect(self.copy_code_btn)  # скопировать
        self.search_edit.textChanged.connect(self.on_text_changed)  # поиск
        self.horizontalSlider.valueChanged.connect(self.change_font_size)  # slider

        self.change_font_size(self.horizontalSlider.value())
        # Стили
        style_text = open('stylee/vertical_layout')
        text = '\n'.join(style_text.read().split('\n'))
        self.setStyleSheet(text)

        style_text = open('stylee/frame')
        text = '\n'.join(style_text.read().split('\n'))
        self.filter_lay.setStyleSheet(text)

        style_text = open('stylee/frame_2')
        text = '\n'.join(style_text.read().split('\n'))
        self.frame_2.setStyleSheet(text)

        style_text = open('stylee/frame_3')
        text = '\n'.join(style_text.read().split('\n'))
        self.frame_2.setStyleSheet(text)

        style_text = open('stylee/table_widget')
        text = '\n'.join(style_text.read().split('\n'))
        self.table.setStyleSheet(text)  # стили для tablewidget

        style_text = open('stylee/text_edit.txt')
        self.textEdit.setWordWrapMode(QTextOption.WrapMode.WordWrap)
        text = '\n'.join(style_text.read().split('\n'))
        self.textEdit.setStyleSheet(text)  # стили для tablewidget

        style_text = open('stylee/hor_layout_6')
        text = '\n'.join(style_text.read().split('\n'))
        self.serach_lay.setStyleSheet(text)
        self.search_edit.setStyleSheet('border-bottom: 1px solid #bc8ebd; padding: 2px;''')
        text = '''QPushButton {
border-radius: 4px;
                }
QPushButton:hover {
background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.971591, y2:0, stop:0 rgba(162, 65, 146,75),
 stop:1 rgba(14, 8, 73, 75));
                }
QPushButton:pressed {
background-color: rgba(185, 0, 185, 150);'''
        self.update_table_bnt.setStyleSheet(text)
        self.Add_s.setStyleSheet(text)
        self.copy_code_button.setStyleSheet(text)
        self.clear_button.setStyleSheet(text)

    def add_s(self):  # Создаем экземпляр и запускаем второе окно
        self.second_window = SecondWindow(status='new_s')
        self.second_window.show()

    def update_table(self):  # обновление таблицы
        self.table.clearContents()
        if self.current_check_button == "Всё":
            list_tag = self.SQL.get_all_templates()
        else:
            list_tag = self.SQL.get_some_templates(self.current_check_button)
        self.table.setRowCount(len(list_tag))
        for id_elem, elem in enumerate(list_tag):
            for id_row, row in enumerate(elem):
                self.table.setItem(id_elem, id_row, QTableWidgetItem(str(row)))
                self.table.show()

    def check_btn_group(self):
        self.current_check_button = self.check_button_group.checkedButton().text()
        print(self.current_check_button)
        self.update_table()

    def form_frame(self):  # Формирование фильтров
        tags = self.SQL.get_tags()
        button_name = []
        for elem in tags:
            if elem[0] not in button_name:
                btn = QRadioButton(f'{elem[0]}', self)
                btn.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
                btn.setStyleSheet('border: 0px;')
                self.horizontalLayout.addWidget(btn)
                self.check_button_group.addButton(btn)
                buttons = self.check_button_group.buttons()
                button_name = [button.text() for button in buttons]
                btn.show()
        for radio in self.check_button_group.buttons():
            radio.setStyleSheet('''QRadioButton:indicator{
                                                                    border: 2px solid #bc8ebd;
                                                                    background-color: transparent;
                                                                     /* Прозрачный фон для индикации */
                                                                    border-radius:8px; }
                                        QRadioButton::indicator:checked{
                                                                    background-color: #653066;
                                                                    border: 1px solid #bc8ebd;
                                                                    border-radius:8px; }

                                ''')

    def on_item_click(self, item):  # нажатие на шаблон
        current_cursor = self.textEdit.textCursor()  # Получаем текущий курсор
        row = item.row()  # Получаем номер строки
        a = self.table.item(row, 1).text()
        code = self.SQL.update_template_by_title(a)
        code = list(code)[0][0]
        current_cursor.insertText(str(code))

    def clear_btn(self):
        self.textEdit.clear()

    def copy_code_btn(self):
        text = self.textEdit.toPlainText()
        clipboard = QApplication.clipboard()
        clipboard.setText(text)

    def on_text_changed(self, text):
        # Убираем подсветку для всех строк
        for row in range(self.table.rowCount()):
            for column in range(self.table.columnCount()):
                item = self.table.item(row, column)
                if item is not None:
                    item.setBackground(self.table.palette().window())  # Сброс цвета фона
        # Если текст пустой, выходим из метода
        if not text:
            return
        # Подсвечиваем строки, если есть совпадение
        for row in range(self.table.rowCount()):
            title_item = self.table.item(row, 1)
            if title_item and text.lower() in title_item.text().lower():  # Сравнение с учетом регистра
                title_item.setBackground(QColor(255, 105, 180, 50))

    def change_font_size(self, value):
        text = self.textEdit.toPlainText()
        self.textEdit.clear()
        font = self.textEdit.font()  # Получаем текущий шрифт текстового редактора
        font.setPointSize(value)  # Устанавливаем новый размер шрифта
        self.textEdit.setFontPointSize(font.pointSize())
        self.textEdit.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
