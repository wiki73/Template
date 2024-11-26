import sqlite3

from PyQt6.QtWidgets import QWidget

from desinger_file.add_s import Ui_Form
from sql import SQL


class SecondWindow(QWidget, Ui_Form):  # окно дабавить шаблон
    def __init__(self, status=None, tag_for_change=None, name_for_change=None, code_for_change=None):
        super().__init__()
        self.setupUi(self)
        self.SQL = SQL()
        self.status = status
        self.tag_for_change = tag_for_change
        self.name_for_change = name_for_change
        self.code_for_change = code_for_change

        if self.status == 'change_s':
            self.tag_line.setText(self.tag_for_change)
            self.Name_line.setText(self.name_for_change)
            self.code_edit.setPlainText(self.code_for_change)
        self.add_s_btn.clicked.connect(self.add_s_button)


    def add_s_button(self):
        if self.status == 'new_s':
            code_text = self.code_edit.toPlainText()
            tag_text = self.tag_line.text()
            name_text = self.Name_line.text()
            try:
                self.SQL.insert_s_table(tag_text, name_text)  # добавление в бд в s_table новый tag и новый title

                self.SQL.insert_code_table(name_text, code_text)  # добавление в бд в code_table новый код
            except sqlite3.Error:
                print('Ошибка sqlite3.Error')
            self.code_edit.clear()
            self.tag_line.clear()
            self.Name_line.clear()
        elif self.status == 'change_s':
            code_text = self.code_edit.toPlainText()
            tag_text = self.tag_line.text()
            name_text = self.Name_line.text()
            try:
                self.SQL.delete_by_title(self.name_for_change)
                self.SQL.insert_s_table(tag_text, name_text)
                self.SQL.insert_code_table(name_text, code_text)  # добавление в бд в code_table новый код
            except sqlite3.Error:
                print('Ошибка sqlite3.Error')
            self.add_s_btn.clicked.connect(self.close)
