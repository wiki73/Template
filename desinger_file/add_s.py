# Form implementation generated from reading ui file 'ui_file\add_s_widget.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        Form.resize(618, 468)
        Form.setMinimumSize(QtCore.QSize(0, 468))
        Form.setStyleSheet("")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 15, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.Name_line = QtWidgets.QLineEdit(parent=Form)
        self.Name_line.setObjectName("Name_line")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Name_line)
        self.tag_line = QtWidgets.QLineEdit(parent=Form)
        self.tag_line.setObjectName("tag_line")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.tag_line)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_2)
        self.verticalLayout.addLayout(self.formLayout)
        self.add_s_btn = QtWidgets.QPushButton(parent=Form)
        self.add_s_btn.setStyleSheet("")
        self.add_s_btn.setObjectName("add_s_btn")
        self.verticalLayout.addWidget(self.add_s_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.code_edit = QtWidgets.QTextEdit(parent=Form)
        self.code_edit.setObjectName("code_edit")
        self.horizontalLayout_2.addWidget(self.code_edit)
        self.horizontalLayout_2.setStretch(0, 2)
        self.horizontalLayout_2.setStretch(1, 5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Tag"))
        self.label_2.setText(_translate("Form", "Name"))
        self.add_s_btn.setText(_translate("Form", "Добавить шаблон"))
