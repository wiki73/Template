# Form implementation generated from reading ui file 'ui_file\main.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1221, 783)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("")
        self.main_lwidget = QtWidgets.QWidget(parent=MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_lwidget.sizePolicy().hasHeightForWidth())
        self.main_lwidget.setSizePolicy(sizePolicy)
        self.main_lwidget.setBaseSize(QtCore.QSize(0, 0))
        self.main_lwidget.setMouseTracking(False)
        self.main_lwidget.setStyleSheet("")
        self.main_lwidget.setObjectName("main_lwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_lwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.filter_lay = QtWidgets.QFrame(parent=self.main_lwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_lay.sizePolicy().hasHeightForWidth())
        self.filter_lay.setSizePolicy(sizePolicy)
        self.filter_lay.setMaximumSize(QtCore.QSize(1221, 150))
        self.filter_lay.setStyleSheet("")
        self.filter_lay.setObjectName("filter_lay")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.filter_lay)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.all = QtWidgets.QRadioButton(parent=self.filter_lay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.all.sizePolicy().hasHeightForWidth())
        self.all.setSizePolicy(sizePolicy)
        self.all.setAcceptDrops(False)
        self.all.setAutoFillBackground(False)
        self.all.setStyleSheet("")
        self.all.setChecked(True)
        self.all.setObjectName("all")
        self.check_button_group = QtWidgets.QButtonGroup(MainWindow)
        self.check_button_group.setObjectName("check_button_group")
        self.check_button_group.addButton(self.all)
        self.horizontalLayout.addWidget(self.all)
        self.verticalLayout.addWidget(self.filter_lay)
        self.main_horizantal = QtWidgets.QHBoxLayout()
        self.main_horizantal.setObjectName("main_horizantal")
        self.tab_lay = QtWidgets.QFrame(parent=self.main_lwidget)
        self.tab_lay.setObjectName("tab_lay")
        self.table_lay = QtWidgets.QVBoxLayout(self.tab_lay)
        self.table_lay.setSpacing(0)
        self.table_lay.setObjectName("table_lay")
        self.serach_lay = QtWidgets.QFrame(parent=self.tab_lay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.serach_lay.sizePolicy().hasHeightForWidth())
        self.serach_lay.setSizePolicy(sizePolicy)
        self.serach_lay.setObjectName("serach_lay")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.serach_lay)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_search = QtWidgets.QLabel(parent=self.serach_lay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_search.sizePolicy().hasHeightForWidth())
        self.label_search.setSizePolicy(sizePolicy)
        self.label_search.setStyleSheet("font-size: 16px")
        self.label_search.setObjectName("label_search")
        self.horizontalLayout_4.addWidget(self.label_search)
        self.search_edit = QtWidgets.QLineEdit(parent=self.serach_lay)
        self.search_edit.setStyleSheet("border-color: 2px solid rgb(255, 0, 17);")
        self.search_edit.setObjectName("search_edit")
        self.horizontalLayout_4.addWidget(self.search_edit)
        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 4)
        self.table_lay.addWidget(self.serach_lay)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.table_lay.addLayout(self.verticalLayout_2)
        self.update_table_bnt = QtWidgets.QPushButton(parent=self.tab_lay)
        self.update_table_bnt.setStyleSheet("")
        self.update_table_bnt.setObjectName("update_table_bnt")
        self.table_lay.addWidget(self.update_table_bnt)
        self.main_horizantal.addWidget(self.tab_lay)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.textEdit = QtWidgets.QTextEdit(parent=self.main_lwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setBaseSize(QtCore.QSize(0, 0))
        self.textEdit.setStyleSheet("")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout_2.addWidget(self.textEdit)
        self.main_horizantal.addLayout(self.horizontalLayout_2)
        self.right_lay = QtWidgets.QFrame(parent=self.main_lwidget)
        self.right_lay.setObjectName("right_lay")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.right_lay)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(parent=self.right_lay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setObjectName("frame_2")
        self.formLayout = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout.setContentsMargins(-1, -1, 10, -1)
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.clear_button = QtWidgets.QPushButton(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_button.sizePolicy().hasHeightForWidth())
        self.clear_button.setSizePolicy(sizePolicy)
        self.clear_button.setObjectName("clear_button")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.clear_button)
        self.copy_code_button = QtWidgets.QPushButton(parent=self.frame_2)
        self.copy_code_button.setObjectName("copy_code_button")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.copy_code_button)
        self.horizontalSlider = QtWidgets.QSlider(parent=self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalSlider.sizePolicy().hasHeightForWidth())
        self.horizontalSlider.setSizePolicy(sizePolicy)
        self.horizontalSlider.setStyleSheet("border: 0px;")
        self.horizontalSlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.horizontalSlider)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.button_lay = QtWidgets.QVBoxLayout()
        self.button_lay.setObjectName("button_lay")
        self.Add_s = QtWidgets.QPushButton(parent=self.right_lay)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Add_s.sizePolicy().hasHeightForWidth())
        self.Add_s.setSizePolicy(sizePolicy)
        self.Add_s.setObjectName("Add_s")
        self.button_lay.addWidget(self.Add_s)
        self.verticalLayout_3.addLayout(self.button_lay)
        self.verticalLayout_3.setStretch(0, 20)
        self.verticalLayout_3.setStretch(1, 1)
        self.main_horizantal.addWidget(self.right_lay)
        self.main_horizantal.setStretch(1, 13)
        self.main_horizantal.setStretch(2, 3)
        self.verticalLayout.addLayout(self.main_horizantal)
        MainWindow.setCentralWidget(self.main_lwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.all.setText(_translate("MainWindow", "Всё"))
        self.label_search.setText(_translate("MainWindow", "Поиск"))
        self.update_table_bnt.setText(_translate("MainWindow", "Обновить таблицу"))
        self.clear_button.setText(_translate("MainWindow", "Отчистить"))
        self.copy_code_button.setText(_translate("MainWindow", "Копировать код"))
        self.Add_s.setText(_translate("MainWindow", "Добавить Шаблон"))
