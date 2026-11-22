
from PySide6 import QtCore

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QStackedWidget, QTableWidget, QTableWidgetItem,
    QTreeWidget, QTreeWidgetItem, QVBoxLayout, QWidget,QStyle)

import pickle
import pandas
import numpy




class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(893, 569)
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.treeWidget = QTreeWidget(self.page)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"CELLS");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.dir_icon = QApplication.style().standardIcon(QStyle.SP_DirIcon);
        with open("cell.txt", "r") as file:
            a = file.readlines()
            b = []
            for i in list(a):
                b.append(i[:-1:])
            for i in b:
                self.treeWidgetitem = QTreeWidgetItem(self.treeWidget,[i])
                self.treeWidgetitem.setIcon(0,self.dir_icon)
                self.treeWidgetitem.addChild(QTreeWidgetItem(["Plate1"]))
                self.treeWidgetitem.addChild(QTreeWidgetItem(["Plate2"]))
                self.treeWidgetitem.addChild(QTreeWidgetItem(["Plate3"]))
                self.treeWidgetitem.addChild(QTreeWidgetItem(["Plate4"]))
                self.treeWidgetitem.child(0).setIcon(0,self.dir_icon)
                self.treeWidgetitem.child(1).setIcon(0,self.dir_icon)
                self.treeWidgetitem.child(2).setIcon(0,self.dir_icon)
                self.treeWidgetitem.child(3).setIcon(0,self.dir_icon)


        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.itemClicked.connect(self.onItemClicke)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")
        
        self.pushButton.setIcon(self.pushButton.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.pushButton.clicked.connect(self.buttonpress)



        self.verticalLayout_3.addWidget(self.pushButton)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.page_2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.listWidget = QListWidget(self.page_2)
        self.listWidget.setObjectName(u"listWidget")


        self.listWidget.itemClicked.connect(self.clicklist)
        self.listWidget.setFont(QFont("Times",12))
        




        self.horizontalLayout_2.addWidget(self.listWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.gridLayout_2.addLayout(self.verticalLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)



        self.page_3 = QWidget()

        self.tableWidget33 = QTableWidget(self.page_3)
        #make submission dosyası burada gösterilecek
        #csv to list

        

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_4.addWidget(self.stackedWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")

        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1108)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(["sirna","value"])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        #üstte gösterilen hücrenin id si yazsın

        #s2_w2 isimleri de göster
        
        with open('df_test_log.pkl', 'rb') as f:
            data = pickle.load(f)
            a = list(data.index)
            ind = a.index("HEPG2-08_1_B03")
            values = list(data.iloc[ind])


        for i in range(1108):
            self.tableitem = QTableWidgetItem("sirna_"+str(i))
            self.tableitem.setTextAlignment(Qt.AlignCenter)
            self.tableitem2 = QTableWidgetItem(str(values[i])) 
            self.tableitem2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, self.tableitem)
            self.tableWidget.setItem(i, 1, self.tableitem2)
        self.tableWidget.setFont(QFont("Times",15))

        self.horlayforlabel = QHBoxLayout()
        self.idlabel = QLabel("id: HEPG2-08_1_B03")
        self.sirnalabel = QLabel("sirna: 855")
        
        self.horlayforlabel.addWidget(self.idlabel)
        self.horlayforlabel.addWidget(self.sirnalabel)
        self.verticalLayout.addLayout(self.horlayforlabel)
        self.verticalLayout.addWidget(self.tableWidget)

        self.tableWidget_2 = QTableWidget(Form)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        
        
        self.tableWidget_2.setColumnCount(6)
        self.tableWidget_2.setRowCount(4)
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setVisible(False)

        self.labelphoto = QLabel("PHOTOS:")


        r = 0
        c = 0
        for i in range(1,3):
            for j in range(1,7):
                a = "HEPG2-08"
                b = "1"
                d = "B03"
                path = f"C:/Users/feder/Documents/data/test/{a}/Plate{b}/{d}_s{i}_w{j}"
                path += ".png"
                self.pixm = QPixmap(path)
                self.label = QLabel()
                self.label.setPixmap(self.pixm)
                self.label.setScaledContents(True)
                self.tableWidget_2.setCellWidget(r,c,self.label)
                self.tableWidget_2.setColumnWidth(c,200)
                self.tableWidget_2.setRowHeight(r,200)
                



                c += 1
                
                if c == 6:
                    r += 1
                    c = 0


        self.verticalLayout.addWidget(self.labelphoto)
        self.verticalLayout.addWidget(self.tableWidget_2)


        self.horizontalLayout_4.addLayout(self.verticalLayout)


        self.gridLayout_3.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        #self.pushButton.setText(QCoreApplication.translate("Form", u"go back", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"cells", None))
    # retranslateUi


    @QtCore.Slot(QTreeWidgetItem, int)
    def onItemClicke(self, it, col):
        print(it, col, it.text(col))
        self.stackedWidget.setCurrentIndex(1)
        self.listWidget.clear()
        try:
            hm = it.parent().text(col)
            self.label_3.setText(hm + "/" + it.text(col))
            self.f_icon = QApplication.style().standardIcon(QStyle.SP_FileIcon);

            with open("well.txt") as file:
                a = file.readlines()
                b = []
                for i in a:
                    b.append(i[:-1])
                for i in b:
                    self.listWidget.addItem(QListWidgetItem(self.f_icon,f"{hm}_{it.text(col)[5:]}_"+f"{i}"))
        except:
            hm = it.text(col)
            print(hm)
            import csv

            with open('submission.csv', newline='') as f:
                reader = csv.reader(f)
                data = list(reader)
            self.b = []
            for i in range(len(data)):
                for j in data[i]:
                    self.b.append(j)
            listem = []
            with open("well.txt") as file:
                a = file.readlines()
                a = list(a)
                c = 4
                for i in range(1,c+1):
                    for j in a:
                        hm = it.text(col) + "_" + str(i) + "_"
                        hm += str(j)
                        listem.append(hm)
                       
            for i in listem:
                self.listWidget.addItem(QListWidgetItem(   str(i)[:-1] + "    " + str( self.b[self.b.index(i[:-1]) + 1] )   ))




           


                

    @QtCore.Slot(QListWidgetItem)
    def clicklist(self,it):
        b = it.text()
        with open('df_test_log.pkl', 'rb') as f:
            data = pickle.load(f)
            a = list(data.index)
            ind = a.index(b)
            values = list(data.iloc[ind])


        for i in range(1108):
            self.tableitem = QTableWidgetItem("sirna_"+str(i))
            self.tableitem.setTextAlignment(Qt.AlignCenter)
            self.tableitem2 = QTableWidgetItem(str(values[i])) 
            self.tableitem2.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(i, 0, self.tableitem)
            self.tableWidget.setItem(i, 1, self.tableitem2)


        r = 0
        c = 0
        for i in range(1,3):
            for j in range(1,7):
                d = b.split("_")
                path = f"C:/Users/feder/Documents/data/test/{d[0]}/Plate{d[1]}/{d[2]}_s{i}_w{j}"
                path += ".png"
                self.pixm = QPixmap(path)
                self.label = QLabel()
                self.label.setPixmap(self.pixm)
                self.label.setScaledContents(True)
                self.tableWidget_2.setCellWidget(r,c,self.label)
                self.tableWidget_2.setColumnWidth(c,200)
                self.tableWidget_2.setRowHeight(r,200)
                self.idlabel.setText("id: " + b)
                self.sirnalabel.setText("sirna: " + self.b[self.b.index(b) + 1])


                c += 1
                
                if c == 6:
                    r += 1
                    c = 0









    def buttonpress(self):
        self.stackedWidget.setCurrentIndex(0)











