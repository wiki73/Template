import sqlite3

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem, QMenu, QSizePolicy

from second_window import SecondWindow
from sql import SQL


class Table(QTableWidget):
    def __init__(self):
        super().__init__()
        self.SQL = SQL()
        self.all_templates = self.SQL.get_all_templates()

        self.setColumnCount(2)
        self.setRowCount(len(self.all_templates))
        self.setHorizontalHeaderLabels(["tag", 'Title'])

        header = self.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        for id_elem, elem in enumerate(self.all_templates):
            for id_row, row in enumerate(elem):
                item = QTableWidgetItem(row)
                self.setItem(id_elem, id_row, item)

        self.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, pos):
        context_menu = QMenu(self)
        context_menu.setStyleSheet("""
            QMenu {
                background-color: #bc8ebd;
                border: 1px solid black;
                border-radius: 18px;
                color: rgb(0,0,0);
            }
            QMenu::item {
                padding: 8px 16px;
            }
            QMenu::item:selected {
                background-color: rgba(0,0,0,50);
                color: #dd12e0;
            }
        """)

        remove_action = QAction('Удалить строку', self)

        move_down_action = QAction('Передвинуть вниз', self)
        move_up_action = QAction('Передвинуть вверх', self)

        change_action = QAction('Изменить шаблон', self)

        remove_action.triggered.connect(self.remove_row)
        move_down_action.triggered.connect(self.move_down)
        move_up_action.triggered.connect(self.move_up)
        change_action.triggered.connect(self.change_s)

        context_menu.addAction(remove_action)
        context_menu.addAction(move_up_action)
        context_menu.addAction(move_down_action)
        context_menu.addAction(change_action)

        context_menu.exec(self.viewport().mapToGlobal(pos))

    def remove_row(self):
        current_row = self.currentRow()
        if current_row >= 0:
            # Получаем ID для удаления из базы данных
            tag_item = self.item(current_row, 1)  # Предполагаем, что ID в первом столбце
            if tag_item is not None:
                id_to_delete = tag_item.text()

                # Удаление записи из базы данных
                self.SQL.delete_by_title(id_to_delete)

                # Удаление строки из QTableWidget
                self.removeRow(current_row)

    def move_down(self):
        row = self.currentRow()
        column = self.currentColumn()

        if row < self.rowCount() - 1:
            self.insertRow(row + 2)
            for i in range(self.columnCount()):
                self.setItem(row + 2, i, self.takeItem(row, i))
            self.setCurrentCell(row + 2, column)
            self.removeRow(row)
        self.update_sql_table()

    def move_up(self):
        row = self.currentRow()
        column = self.currentColumn()

        if row > 0:
            self.insertRow(row - 1)
            for i in range(self.columnCount()):
                self.setItem(row - 1, i, self.takeItem(row + 1, i))
            self.setCurrentCell(row - 1, column)
            self.removeRow(row + 1)
        self.update_sql_table()

    def update_sql_table(self):
        elements = []
        for row in range(self.rowCount()):
            a = []
            elem = self.item(row, 0).text()
            elem_1 = self.item(row, 1).text()
            if elem_1 is not None:
                a.append(elem)
                a.append(elem_1)
                elements.append(a)
        self.SQL.delete_s_table()
        for elem in elements:
            tag_text = elem[0]
            name_text = elem[1]
            self.SQL.insert_s_table(str(tag_text), str(name_text))

    def change_s(self):

        row = self.currentRow()
        tag = str(self.item(row, 0).text())
        name = str(self.item(row, 1).text())
        code = self.SQL.code_by_title(name)
        code = str(list(code)[0][0])
        self.second_window = SecondWindow(status='change_s', tag_for_change=tag, name_for_change=name,
                                          code_for_change=code)
        self.second_window.show()

    def update_table(self, current_check_button):  # обновление таблицы
        self.clearContents()
        if current_check_button == "Всё":
            self.SQL.get_all_templates()
        else:
            self.SQL.get_some_templates(current_check_button)
        self.setRowCount(len(self.all_templates))
        for id_elem, elem in enumerate(self.all_templates):
            for id_row, row in enumerate(elem):
                self.setItem(id_elem, id_row, QTableWidgetItem(str(row)))
