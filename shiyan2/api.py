from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QHeaderView
import main
import os
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shuchu = QtWidgets.QTableWidget(self.centralwidget)
        self.shuchu.setGeometry(QtCore.QRect(10, 10, 921, 421))
        self.shuchu.setStyleSheet("QHeaderView{                            /*设置标题(包括垂直+水平的)*/\n"
                                  "    \n"
                                  "              font-size: 19px;                /*11榜*/\n"
                                  "          border: 1px solid rgb(255, 255, 255);\n"
                                  "       /* border-bottom: 2px solid rgb(35, 100, 224);         下边框深蓝色*/\n"
                                  "        background: rgb(100, 188, 238);                /*背景浅蓝色*/ \n"
                                  "          min-height:40px;\n"
                                  "           \n"
                                  "} \n"
                                  " \n"
                                  " \n"
                                  "QHeaderView::section:horizontal {                     /*设置标题(水平的)*/\n"
                                  "        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
                                  "          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
                                  "        color: rgb(2, 65, 132);\n"
                                  "        background: transparent;\n"
                                  "        padding-left: 2px;\n"
                                  "        min-width:60px;\n"
                                  "}\n"
                                  "QHeaderView::section:horizontal:hover {            /*设置鼠标停留状态*/\n"
                                  "        color: white;                            /*字体白色*/\n"
                                  "        background: rgb(11,82,202);                /*背景深蓝色*/\n"
                                  "}\n"
                                  "QHeaderView::section:horizontal:pressed {            /*设置鼠标按下状态*/\n"
                                  "        color: white;\n"
                                  "        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
                                  "}\n"
                                  "QHeaderView::section:vertical {                     /*设置标题(垂直的)*/\n"
                                  "        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
                                  "          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
                                  "        color: rgb(2, 65, 132);\n"
                                  "        background: rgb(255, 255, 255,180);\n"
                                  "        padding-top: 3px;\n"
                                  "        min-width:60px;\n"
                                  "        \n"
                                  "}\n"
                                  "QHeaderView::section:vertical:hover {            /*设置鼠标停留状态*/\n"
                                  "        color: white;                            /*字体白色*/\n"
                                  "        background: rgb(11,82,202);                /*背景深蓝色*/\n"
                                  "}\n"
                                  "QHeaderView::section:vertical:pressed {            /*设置鼠标按下状态*/\n"
                                  "        color: white;\n"
                                  "        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
                                  "}\n"
                                  " \n"
                                  " \n"
                                  "QHeaderView::up-arrow {                        /*设置向上排序指针*/\n"
                                  "        width: 13px;\n"
                                  "        height: 11px;\n"
                                  "        padding-right: 0px;                         /*设置右内边距*/\n"
                                  "        image: url(:/arrow_up.png);\n"
                                  "        subcontrol-position: center right;\n"
                                  "}\n"
                                  "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                                  "     \n"
                                  "}\n"
                                  "QHeaderView::down-arrow {                        /*设置向下排序指针*/\n"
                                  "        width: 13px;\n"
                                  "        height: 11px;\n"
                                  "        padding-right: 10px;\n"
                                  "        image: url(:/arrow_down.png);\n"
                                  "        subcontrol-position: center right;\n"
                                  "}\n"
                                  "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                                  "     \n"
                                  "}\n"
                                  "QTableWidget,QTableView {\n"
                                  "                font-size: 17px;                /*10榜*/                \n"
                                  "                color : rgb(1,37,116);                \n"
                                  "        border: 2px solid rgb(100, 188, 238);        \n"
                                  "        background: rgb(248,248,248);\n"
                                  "        gridline-color: rgb(196,226,255);    \n"
                                  "        text-align: center;    \n"
                                  "        outline:0px;            /*禁止焦点*/\n"
                                  "        \n"
                                  "}\n"
                                  "QTableWidget::item,QTableView::item {                            /*设置视图项*/\n"
                                  "        padding-left: 5px;\n"
                                  "        padding-right: 5px;\n"
                                  "        border: none; \n"
                                  "        background: rgba(251,251,253,200);\n"
                                  "       \n"
                                  "       /* border-right: 1px solid rgb(100, 188, 238); */\n"
                                  "        /*border-bottom: 1px solid rgb(100, 188, 238);*/\n"
                                  "}\n"
                                  "QTableWidget::item:selected,QTableView::item:selected {                    /*设置选中的视图项*/\n"
                                  "        background: rgba(207,230,253,200);\n"
                                  "        color : rgb(1,37,116);                \n"
                                  "}\n"
                                  " \n"
                                  " \n"
                                  "QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
                                  "{ \n"
                                  "    background: rgb(250,250,250); \n"
                                  "}\n"
                                  " \n"
                                  "QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
                                  "{ \n"
                                  "    background: rgb(240,247,254); \n"
                                  "}\n"
                                  "QScrollBar:vertical\n"
                                  "{\n"
                                  "    width:8px;\n"
                                  "    background:rgba(0,0,0,0%);\n"
                                  "    margin:0px,0px,0px,0px;\n"
                                  "    padding-top:9px; \n"
                                  "    padding-bottom:9px;\n"
                                  "}\n"
                                  "QScrollBar::handle:vertical\n"
                                  "{\n"
                                  "    width:8px;\n"
                                  "    background:rgba(0,0,0,25%);\n"
                                  "    border-radius:4px; \n"
                                  "    min-height:20;\n"
                                  "}\n"
                                  "QScrollBar::handle:vertical:hover\n"
                                  "{\n"
                                  "    width:8px;\n"
                                  "    background:rgba(0,0,0,50%);  \n"
                                  "    border-radius:4px;\n"
                                  "    min-height:20;\n"
                                  "}\n"
                                  "QScrollBar::add-line:vertical\n"
                                  "{\n"
                                  "    height:9px;width:8px;\n"
                                  "    border-image:url(:/images/a/3.png);\n"
                                  "    subcontrol-position:bottom;\n"
                                  "}\n"
                                  "QScrollBar::sub-line:vertical\n"
                                  "{\n"
                                  "    height:9px;width:8px;\n"
                                  "    border-image:url(:/images/a/1.png);\n"
                                  "    subcontrol-position:top;\n"
                                  "}\n"
                                  "QScrollBar::add-line:vertical:hover \n"
                                  "{\n"
                                  "    height:9px;width:8px;\n"
                                  "    border-image:url(:/images/a/4.png);\n"
                                  "    subcontrol-position:bottom;\n"
                                  "}\n"
                                  "QScrollBar::sub-line:vertical:hover\n"
                                  "{\n"
                                  "    height:9px;width:8px;\n"
                                  "    border-image:url(:/images/a/2.png);\n"
                                  "    subcontrol-position:top;\n"
                                  "}\n"
                                  "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
                                  "{\n"
                                  "    background:rgba(0,0,0,10%);\n"
                                  "    border-radius:4px;\n"
                                  "}")
        self.shuchu.setObjectName("shuchu")
        self.shuchu.setColumnCount(5)
        self.shuchu.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.shuchu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.shuchu.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.shuchu.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.shuchu.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.shuchu.setHorizontalHeaderItem(4, item)
        self.la1 = QtWidgets.QLineEdit(self.centralwidget)
        self.la1.setGeometry(QtCore.QRect(940, 400, 121, 31))
        self.la1.setToolTip("")
        self.la1.setStyleSheet("background:white;\n"
                               "    padding-left:5px ;\n"
                               "    padding-top:1px ;\n"
                               "    border-bottom-left-radius:3px;\n"
                               "    border-bottom-right-radius:3px;\n"
                               "    border: 1px solid rgb(209 , 209 , 209);\n"
                               "    border-top:transparent;")
        self.la1.setObjectName("la1")
        self.wenjian = QtWidgets.QPushButton(self.centralwidget)
        self.wenjian.setGeometry(QtCore.QRect(1080, 400, 61, 31))
        self.wenjian.setStyleSheet("QPushButton\n"
                                   "{\n"
                                   "    color:white;\n"
                                   "    background-color:rgb(14 , 150 , 254);\n"
                                   "    border-radius:5px;\n"
                                   "    font:15px \"微软雅黑\";\n"
                                   "}\n"
                                   "\n"
                                   ":hover\n"
                                   "{\n"
                                   "    color:white;\n"
                                   "    background-color:rgb(44 , 137 , 255);\n"
                                   "}\n"
                                   "\n"
                                   ":pressed\n"
                                   "{\n"
                                   "    color:white;\n"
                                   "    background-color:rgb(14 , 135 , 228);\n"
                                   "    padding-left:3px;\n"
                                   "    padding-top:3px;\n"
                                   "}")
        self.wenjian.setObjectName("wenjian")
        self.wenben = QtWidgets.QLineEdit(self.centralwidget)
        self.wenben.setGeometry(QtCore.QRect(940, 330, 121, 31))
        self.wenben.setToolTip("")
        self.wenben.setStyleSheet("background:white;\n"
                                  "    padding-left:5px ;\n"
                                  "    padding-top:1px ;\n"
                                  "    border-bottom-left-radius:3px;\n"
                                  "    border-bottom-right-radius:3px;\n"
                                  "    border: 1px solid rgb(209 , 209 , 209);\n"
                                  "    border-top:transparent;")
        self.wenben.setObjectName("wenben")
        self.biao = QtWidgets.QPushButton(self.centralwidget)
        self.biao.setGeometry(QtCore.QRect(1080, 330, 61, 31))
        self.biao.setStyleSheet("QPushButton\n"
                                "{\n"
                                "    color:white;\n"
                                "    background-color:rgb(14 , 150 , 254);\n"
                                "    border-radius:5px;\n"
                                "    font:15px \"微软雅黑\";\n"
                                "}\n"
                                "\n"
                                ":hover\n"
                                "{\n"
                                "    color:white;\n"
                                "    background-color:rgb(44 , 137 , 255);\n"
                                "}\n"
                                "\n"
                                ":pressed\n"
                                "{\n"
                                "    color:white;\n"
                                "    background-color:rgb(14 , 135 , 228);\n"
                                "    padding-left:3px;\n"
                                "    padding-top:3px;\n"
                                "}")
        self.biao.setObjectName("biao")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(950, 290, 161, 31))
        self.label.setStyleSheet("font: 12pt \"楷体\";\n"
                                 "color: rgb(170, 170, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(950, 360, 201, 31))
        self.label_2.setStyleSheet("font: 12pt \"楷体\";\n"
                                   "color: rgb(170, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(10, 440, 1131, 201))
        self.tableWidget_6.setStyleSheet("QHeaderView{                            /*设置标题(包括垂直+水平的)*/\n"
                                         "    \n"
                                         "              font-size: 19px;                /*11榜*/\n"
                                         "          border: 1px solid rgb(255, 255, 255);\n"
                                         "       /* border-bottom: 2px solid rgb(35, 100, 224);         下边框深蓝色*/\n"
                                         "        background: rgb(100, 188, 238);                /*背景浅蓝色*/ \n"
                                         "          min-height:40px;\n"
                                         "           \n"
                                         "} \n"
                                         " \n"
                                         " \n"
                                         "QHeaderView::section:horizontal {                     /*设置标题(水平的)*/\n"
                                         "        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
                                         "          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
                                         "        color: rgb(2, 65, 132);\n"
                                         "        background: transparent;\n"
                                         "        padding-left: 2px;\n"
                                         "        min-width:60px;\n"
                                         "}\n"
                                         "QHeaderView::section:horizontal:hover {            /*设置鼠标停留状态*/\n"
                                         "        color: white;                            /*字体白色*/\n"
                                         "        background: rgb(11,82,202);                /*背景深蓝色*/\n"
                                         "}\n"
                                         "QHeaderView::section:horizontal:pressed {            /*设置鼠标按下状态*/\n"
                                         "        color: white;\n"
                                         "        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
                                         "}\n"
                                         "QHeaderView::section:vertical {                     /*设置标题(垂直的)*/\n"
                                         "        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
                                         "          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
                                         "        color: rgb(2, 65, 132);\n"
                                         "        background: rgb(255, 255, 255,180);\n"
                                         "        padding-top: 3px;\n"
                                         "        min-width:60px;\n"
                                         "        \n"
                                         "}\n"
                                         "QHeaderView::section:vertical:hover {            /*设置鼠标停留状态*/\n"
                                         "        color: white;                            /*字体白色*/\n"
                                         "        background: rgb(11,82,202);                /*背景深蓝色*/\n"
                                         "}\n"
                                         "QHeaderView::section:vertical:pressed {            /*设置鼠标按下状态*/\n"
                                         "        color: white;\n"
                                         "        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
                                         "}\n"
                                         " \n"
                                         " \n"
                                         "QHeaderView::up-arrow {                        /*设置向上排序指针*/\n"
                                         "        width: 13px;\n"
                                         "        height: 11px;\n"
                                         "        padding-right: 0px;                         /*设置右内边距*/\n"
                                         "        image: url(:/arrow_up.png);\n"
                                         "        subcontrol-position: center right;\n"
                                         "}\n"
                                         "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                                         "     \n"
                                         "}\n"
                                         "QHeaderView::down-arrow {                        /*设置向下排序指针*/\n"
                                         "        width: 13px;\n"
                                         "        height: 11px;\n"
                                         "        padding-right: 10px;\n"
                                         "        image: url(:/arrow_down.png);\n"
                                         "        subcontrol-position: center right;\n"
                                         "}\n"
                                         "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                                         "     \n"
                                         "}\n"
                                         "QTableWidget,QTableView {\n"
                                         "                font-size: 17px;                /*10榜*/                \n"
                                         "                color : rgb(1,37,116);                \n"
                                         "        border: 2px solid rgb(100, 188, 238);        \n"
                                         "        background: rgb(248,248,248);\n"
                                         "        gridline-color: rgb(196,226,255);    \n"
                                         "        text-align: center;    \n"
                                         "        outline:0px;            /*禁止焦点*/\n"
                                         "        \n"
                                         "}\n"
                                         "QTableWidget::item,QTableView::item {                            /*设置视图项*/\n"
                                         "        padding-left: 5px;\n"
                                         "        padding-right: 5px;\n"
                                         "        border: none; \n"
                                         "        background: rgba(251,251,253,200);\n"
                                         "       \n"
                                         "       /* border-right: 1px solid rgb(100, 188, 238); */\n"
                                         "        /*border-bottom: 1px solid rgb(100, 188, 238);*/\n"
                                         "}\n"
                                         "QTableWidget::item:selected,QTableView::item:selected {                    /*设置选中的视图项*/\n"
                                         "        background: rgba(207,230,253,200);\n"
                                         "        color : rgb(1,37,116);                \n"
                                         "}\n"
                                         " \n"
                                         " \n"
                                         "QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
                                         "{ \n"
                                         "    background: rgb(250,250,250); \n"
                                         "}\n"
                                         " \n"
                                         "QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
                                         "{ \n"
                                         "    background: rgb(240,247,254); \n"
                                         "}\n"
                                         "QScrollBar:vertical\n"
                                         "{\n"
                                         "    width:8px;\n"
                                         "    background:rgba(0,0,0,0%);\n"
                                         "    margin:0px,0px,0px,0px;\n"
                                         "    padding-top:9px; \n"
                                         "    padding-bottom:9px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical\n"
                                         "{\n"
                                         "    width:8px;\n"
                                         "    background:rgba(0,0,0,25%);\n"
                                         "    border-radius:4px; \n"
                                         "    min-height:20;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:hover\n"
                                         "{\n"
                                         "\n"
                                         "    background:rgba(0,0,0,50%);  \n"
                                         "    border-radius:4px;\n"
                                         "    min-height:20;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical\n"
                                         "{\n"
                                         "    height:9px;width:8px;\n"
                                         "    border-image:url(:/images/a/3.png);\n"
                                         "    subcontrol-position:bottom;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical\n"
                                         "{\n"
                                         "    height:9px;width:8px;\n"
                                         "    border-image:url(:/images/a/1.png);\n"
                                         "    subcontrol-position:top;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:hover \n"
                                         "{\n"
                                         "    height:9px;width:8px;\n"
                                         "    border-image:url(:/images/a/4.png);\n"
                                         "    subcontrol-position:bottom;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:hover\n"
                                         "{\n"
                                         "    height:9px;width:8px;\n"
                                         "    border-image:url(:/images/a/2.png);\n"
                                         "    subcontrol-position:top;\n"
                                         "}\n"
                                         "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
                                         "{\n"
                                         "    background:rgba(0,0,0,10%);\n"
                                         "    border-radius:4px;\n"
                                         "}")
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(3)
        self.tableWidget_6.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(10, 650, 1131, 241))
        self.tableWidget_7.setStyleSheet("QHeaderView{                            /*设置标题(包括垂直+水平的)*/\n"
                                         "    \n"
                                         "              font-size: 19px;                /*11榜*/\n"
                                         "          border: 1px solid rgb(255, 255, 255);\n"
                                         "       /* border-bottom: 2px solid rgb(35, 100, 224);         下边框深蓝色*/\n"
                                         "        background: rgb(100, 188, 238);                /*背景浅蓝色*/ \n"
                                         "          min-height:40px;\n"
                                         "           \n"
                                         "} \n"
                                         " \n"
                                         " \n"
                                         "QHeaderView::section:horizontal {                     /*设置标题(水平的)*/\n"
                                         "        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
                                         "          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
                                         "        color: rgb(2, 65, 132);\n"
                                         "        background: transparent;\n"
                                         "        padding-left: 2px;\n"
                                         "        min-width:60px;\n"
                                         "}\n"
                                         "QHeaderView::section:horizontal:hover {            /*设置鼠标停留状态*/\n"
                                         "        color: white;                            /*字体白色*/\n"
                                         "        background: rgb(11,82,202);                /*背景深蓝色*/\n"
                                         "}\n"
                                         "QHeaderView::section:horizontal:pressed {            /*设置鼠标按下状态*/\n"
                                         "        color: white;\n"
                                         "        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
                                         "}\n"
                                         "QHeaderView::section:vertical {                     /*设置标题(垂直的)*/\n"
                                         "        border: 1px solid rgb(255, 255, 255);             /*白色间隔*/\n"
                                         "          border-bottom: 0px;                            /*下边框不需要颜色*/\n"
                                         "        color: rgb(2, 65, 132);\n"
                                         "        background: rgb(255, 255, 255,180);\n"
                                         "        padding-top: 3px;\n"
                                         "        min-width:60px;\n"
                                         "        \n"
                                         "}\n"
                                         "QHeaderView::section:vertical:hover {            /*设置鼠标停留状态*/\n"
                                         "        color: white;                            /*字体白色*/\n"
                                         "        background: rgb(11,82,202);                /*背景深蓝色*/\n"
                                         "}\n"
                                         "QHeaderView::section:vertical:pressed {            /*设置鼠标按下状态*/\n"
                                         "        color: white;\n"
                                         "        background: rgb(39,106,220);                /*背景深蓝色减一点*/\n"
                                         "}\n"
                                         " \n"
                                         " \n"
                                         "QHeaderView::up-arrow {                        /*设置向上排序指针*/\n"
                                         "        width: 13px;\n"
                                         "        height: 11px;\n"
                                         "        padding-right: 0px;                         /*设置右内边距*/\n"
                                         "        image: url(:/arrow_up.png);\n"
                                         "        subcontrol-position: center right;\n"
                                         "}\n"
                                         "QHeaderView::up-arrow:hover, QHeaderView::up-arrow:pressed {\n"
                                         "     \n"
                                         "}\n"
                                         "QHeaderView::down-arrow {                        /*设置向下排序指针*/\n"
                                         "        width: 13px;\n"
                                         "        height: 11px;\n"
                                         "        padding-right: 10px;\n"
                                         "        image: url(:/arrow_down.png);\n"
                                         "        subcontrol-position: center right;\n"
                                         "}\n"
                                         "QHeaderView::down-arrow:hover, QHeaderView::down-arrow:pressed {\n"
                                         "     \n"
                                         "}\n"
                                         "QTableWidget,QTableView {\n"
                                         "                font-size: 17px;                /*10榜*/                \n"
                                         "                color : rgb(1,37,116);                \n"
                                         "        border: 2px solid rgb(100, 188, 238);        \n"
                                         "        background: rgb(248,248,248);\n"
                                         "        gridline-color: rgb(196,226,255);    \n"
                                         "        text-align: center;    \n"
                                         "        outline:0px;            /*禁止焦点*/\n"
                                         "        \n"
                                         "}\n"
                                         "QTableWidget::item,QTableView::item {                            /*设置视图项*/\n"
                                         "        padding-left: 5px;\n"
                                         "        padding-right: 5px;\n"
                                         "        border: none; \n"
                                         "        background: rgba(251,251,253,200);\n"
                                         "       \n"
                                         "       /* border-right: 1px solid rgb(100, 188, 238); */\n"
                                         "        /*border-bottom: 1px solid rgb(100, 188, 238);*/\n"
                                         "}\n"
                                         "QTableWidget::item:selected,QTableView::item:selected {                    /*设置选中的视图项*/\n"
                                         "        background: rgba(207,230,253,200);\n"
                                         "        color : rgb(1,37,116);                \n"
                                         "}\n"
                                         " \n"
                                         " \n"
                                         "QTableView::item:alternate:!selected,QTableWidget::item:alternate:!selected,QListView::item:alternate:!selected \n"
                                         "{ \n"
                                         "    background: rgb(250,250,250); \n"
                                         "}\n"
                                         " \n"
                                         "QTableView::item:!alternate:!selected,QTableWidget::item:!alternate:!selected\n"
                                         "{ \n"
                                         "    background: rgb(240,247,254); \n"
                                         "}\n"
                                         "QScrollBar:vertical\n"
                                         "{\n"
                                         "    width:8px;\n"
                                         "    background:rgba(0,0,0,0%);\n"
                                         "    margin:0px,0px,0px,0px;\n"
                                         "    padding-top:9px; \n"
                                         "    padding-bottom:9px;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical\n"
                                         "{\n"
                                         "    width:8px;\n"
                                         "    background:rgba(0,0,0,25%);\n"
                                         "    border-radius:4px; \n"
                                         "    min-height:20;\n"
                                         "}\n"
                                         "QScrollBar::handle:vertical:hover\n"
                                         "{\n"
                                         "    width:8px;\n"
                                         "    background:rgba(0,0,0,50%);  \n"
                                         "    border-radius:4px;\n"
                                         "    min-height:20;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical\n"
                                         "{\n"
                                         "    height:9px;width:8px;\n"
                                         "    border-image:url(:/images/a/3.png);\n"
                                         "    subcontrol-position:bottom;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical\n"
                                         "{\n"
                                         "    height:9px;width:8px;\n"
                                         "    border-image:url(:/images/a/1.png);\n"
                                         "    subcontrol-position:top;\n"
                                         "}\n"
                                         "QScrollBar::add-line:vertical:hover \n"
                                         "{\n"
                                         "    height:9px;width:8px;\n"
                                         "    border-image:url(:/images/a/4.png);\n"
                                         "    subcontrol-position:bottom;\n"
                                         "}\n"
                                         "QScrollBar::sub-line:vertical:hover\n"
                                         "{\n"
                                         "    height:9px;width:8px;\n"
                                         "    border-image:url(:/images/a/2.png);\n"
                                         "    subcontrol-position:top;\n"
                                         "}\n"
                                         "QScrollBar::add-page:vertical,QScrollBar::sub-page:vertical\n"
                                         "{\n"
                                         "    background:rgba(0,0,0,10%);\n"
                                         "    border-radius:4px;\n"
                                         "}")
        self.tableWidget_7.setObjectName("tableWidget_7")
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.tableWidget_7.setColumnCount(0)
        self.tableWidget_7.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.wenjian.clicked.connect(lambda: self.wenj(MainWindow))
        self.biao.clicked.connect(lambda: self.bia(MainWindow))
        self.tableWidget_6.verticalHeader().setHidden(True)
        self.shuchu.verticalHeader().setHidden(True)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_7.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.shuchu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.shuchu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "步骤"))
        item = self.shuchu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "分析栈"))
        item = self.shuchu.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "剩余输入串"))
        item = self.shuchu.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "所用产生式"))
        item = self.shuchu.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "动作"))
        self.wenjian.setText(_translate("MainWindow", "分析"))
        self.biao.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "请输入合法文本："))
        self.label_2.setText(_translate("MainWindow", "请输入待分析符号串："))
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "非终结符"))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First集"))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Follow集"))

    def bia(self, MainWindow):
        if os.path.exists(self.wenben.text()) is False:
            QMessageBox.critical(MainWindow, "错误", "打开文件失败！",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        else:
            ret = main.Grammar(self.wenben.text())
            PredictTable = ret.getPredictTable()
            NonTerminater = ret.getNonTerminater()
            Terminater = ret.getTerminater()
            Follow = ret.getFollow()
            First = ret.getFirst()
            t = 1
            self.tableWidget_6.setColumnCount(3)
            self.tableWidget_6.setRowCount(len(NonTerminater))
            for i in NonTerminater:
                fir = ''
                fol = ''
                for j in Follow[i]:
                    if j == '':
                        continue
                    fol += ', ' + j
                for j in First[i]:
                    if j == '':
                        continue
                    fir += ', ' + j
                fol = fol[1:]
                fir = fir[1:]
                s1 = 'FIRST(' + i + ') : {' + fir + ' }'
                s2 = 'FOLLOW(' + i + ') : {' + fol + ' }'
                self.tableWidget_6.setItem(t - 1, 1, QTableWidgetItem(s1))
                self.tableWidget_6.setItem(t - 1, 2, QTableWidgetItem(s2))
                self.tableWidget_6.setItem(t - 1, 0, QTableWidgetItem(i))
                t += 1
            t = 1
            self.tableWidget_7.setColumnCount(len(Terminater))
            self.tableWidget_7.setRowCount(len(NonTerminater))
            self.tableWidget_7.setHorizontalHeaderLabels(Terminater)
            self.tableWidget_7.setVerticalHeaderLabels(NonTerminater)
            for j in range(len(NonTerminater)):
                r = PredictTable[NonTerminater[j]]
                for i in range(len(Terminater)):
                    rr = r.get(Terminater[i])
                    self.tableWidget_7.setItem(j, i, QTableWidgetItem(rr))

    def wenj(self, MainWindow):
        if os.path.exists(self.wenben.text()) is False:
            QMessageBox.critical(MainWindow, "错误", "打开文件失败！",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if self.la1.text() == '':
            QMessageBox.critical(MainWindow, "错误", "请输入分析串",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        result, y = main.StackSlove(self.la1.text(), self.wenben.text())
        if y is False:
            QMessageBox.critical(MainWindow, "错误", "无法进行分析",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        else:
            self.shuchu.setColumnCount(5)
            self.shuchu.setRowCount(len(result))
            for i in range(len(result)):
                self.shuchu.setItem(i, 0, QTableWidgetItem(str(i)))
                self.shuchu.setItem(i, 1, QTableWidgetItem(result[i][0]))
                self.shuchu.setItem(i, 2, QTableWidgetItem(result[i][1]))
                self.shuchu.setItem(i, 3, QTableWidgetItem(result[i][2]))
                self.shuchu.setItem(i, 4, QTableWidgetItem(result[i][3]))


def go():
    app = QtWidgets.QApplication(sys.argv)
    aw = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    aw.setupUi(w)
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    go()
