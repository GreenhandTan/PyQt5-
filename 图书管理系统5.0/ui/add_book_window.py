# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_book_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(267, 222)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(72, 0))
        self.label.setStyleSheet("font: 12pt \"宋体\";")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.book_name_lineEdit = QtWidgets.QLineEdit(Form)
        self.book_name_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.book_name_lineEdit.setObjectName("book_name_lineEdit")
        self.horizontalLayout.addWidget(self.book_name_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(72, 0))
        self.label_2.setStyleSheet("font: 12pt \"宋体\";")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.author_lineEdit = QtWidgets.QLineEdit(Form)
        self.author_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.author_lineEdit.setObjectName("author_lineEdit")
        self.horizontalLayout_2.addWidget(self.author_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(72, 0))
        self.label_3.setStyleSheet("font: 12pt \"宋体\";")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.publish_company_lineEdit = QtWidgets.QLineEdit(Form)
        self.publish_company_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.publish_company_lineEdit.setObjectName("publish_company_lineEdit")
        self.horizontalLayout_3.addWidget(self.publish_company_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setStyleSheet("font: 12pt \"宋体\";")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.publish_date_lineEdit = QtWidgets.QLineEdit(Form)
        self.publish_date_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.publish_date_lineEdit.setObjectName("publish_date_lineEdit")
        self.horizontalLayout_4.addWidget(self.publish_date_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setStyleSheet("font: 12pt \"宋体\";")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.store_num_lineEdit = QtWidgets.QLineEdit(Form)
        self.store_num_lineEdit.setStyleSheet("font: 12pt \"宋体\";")
        self.store_num_lineEdit.setObjectName("store_num_lineEdit")
        self.horizontalLayout_5.addWidget(self.store_num_lineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.add_book_pushButton = QtWidgets.QPushButton(Form)
        self.add_book_pushButton.setStyleSheet("font: 12pt \"宋体\";")
        self.add_book_pushButton.setObjectName("add_book_pushButton")
        self.horizontalLayout_6.addWidget(self.add_book_pushButton)

        # 爬虫添加图书按钮
        self.add_book_pushButton_2 = QtWidgets.QPushButton(Form)
        self.add_book_pushButton_2.setStyleSheet("font: 12pt \"宋体\";")
        self.add_book_pushButton_2.setObjectName("add_book_pushButton_2")
        self.horizontalLayout_6.addWidget(self.add_book_pushButton_2)

        self.gridLayout.addLayout(self.horizontalLayout_6, 5, 0, 1, 1)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "书    名:"))
        self.label_2.setText(_translate("Form", "作    者:"))
        self.label_3.setText(_translate("Form", "出 版 社:"))
        self.label_4.setText(_translate("Form", "出版日期:"))
        self.label_5.setText(_translate("Form", "库存数量:"))
        self.add_book_pushButton.setText(_translate("Form", "普通添加"))
        self.add_book_pushButton_2.setText(_translate("Form", "批量添加"))
