from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox, QHeaderView
import main
import os
import sys
IsOpen = False


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1153, 898)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.shuchu = QtWidgets.QTableWidget(self.centralwidget)
        self.shuchu.setGeometry(QtCore.QRect(10, 10, 441, 421))
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
        self.shuchu.setColumnCount(2)
        self.shuchu.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.shuchu.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.shuchu.setHorizontalHeaderItem(1, item)
        self.la1 = QtWidgets.QLineEdit(self.centralwidget)
        self.la1.setGeometry(QtCore.QRect(10, 560, 121, 31))
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
        self.wenjian.setGeometry(QtCore.QRect(150, 560, 61, 31))
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
        self.wenben.setGeometry(QtCore.QRect(10, 490, 121, 31))
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
        self.biao.setGeometry(QtCore.QRect(150, 490, 61, 31))
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
        self.label.setGeometry(QtCore.QRect(20, 450, 161, 31))
        self.label.setStyleSheet("font: 12pt \"楷体\";\n"
                                 "color: rgb(170, 170, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 520, 201, 31))
        self.label_2.setStyleSheet("font: 12pt \"楷体\";\n"
                                   "color: rgb(170, 170, 255);")
        self.label_2.setObjectName("label_2")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_6.setGeometry(QtCore.QRect(460, 10, 681, 421))
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
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.tableWidget_7 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_7.setGeometry(QtCore.QRect(220, 440, 921, 451))
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
        self.tableWidget_7.setColumnCount(5)
        self.tableWidget_7.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.wenjian.clicked.connect(lambda: self.wenj(MainWindow))
        self.biao.clicked.connect(lambda: self.bia(MainWindow))
        self.shuchu.verticalHeader().setHidden(True)
        self.tableWidget_6.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_7.horizontalHeader().setStretchLastSection(True)
        self.shuchu.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.shuchu.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "所选文法"))
        item = self.shuchu.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "First集"))
        self.wenjian.setText(_translate("MainWindow", "分析"))
        self.biao.setText(_translate("MainWindow", "确定"))
        self.label.setText(_translate("MainWindow", "请输入合法文本："))
        self.label_2.setText(_translate("MainWindow", "请输入待分析符号串："))
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "步骤"))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "状态栈"))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "符号栈"))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "输入串"))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "动作说明"))

    def bia(self, MainWindow):
        global IsOpen
        if os.path.exists(self.wenben.text()) is False:
            QMessageBox.critical(MainWindow, "错误", "打开文件失败！",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        else:
            Lr = main.LR1Grammar(self.wenben.text())
            self.Lr = Lr
            IsOpen = True
            terminater = Lr.GetTerminater()
            terminater.append("#")
            nonterminater = Lr.GetNonTerminater()
            first = Lr.GetFirst()
            actionTable = Lr.GetActionTable()
            GOTOtable = Lr.GetGOTOtable()
            grammar2 = Lr.GetGrammar2()
            self.shuchu.setColumnCount(2)
            self.shuchu.setRowCount(len(nonterminater))
            projectSetFamily = Lr.GetProjectSetFamily()
            for i in range(len(grammar2)):
                s1 = "|".join(grammar2[nonterminater[i]])
                self.shuchu.setItem(i, 0, QTableWidgetItem(
                    nonterminater[i] + "->" + s1))
                s2 = "FIRST({}):({})".format(
                    nonterminater[i], ",".join(first[nonterminater[i]]))
                self.shuchu.setItem(i, 1, QTableWidgetItem(s2))
            n = len(terminater)
            nonterminater = nonterminater[1:]
            location = {}
            self.tableWidget_6.setColumnCount(
                len(terminater) + len(nonterminater))
            self.tableWidget_6.setRowCount(len(projectSetFamily))
            for i in range(n):
                location[terminater[i]] = i
                self.tableWidget_6.setHorizontalHeaderItem(
                    i, QTableWidgetItem(terminater[i]))
            for i in range(len(nonterminater)):
                j = n + i
                location[nonterminater[i]] = j
                self.tableWidget_6.setHorizontalHeaderItem(
                    j, QTableWidgetItem(nonterminater[i]))
            for i in range(len(projectSetFamily)):
                self.tableWidget_6.setVerticalHeaderItem(
                    i, QTableWidgetItem(str(i)))
                for j in range(n):
                    if actionTable[i][terminater[j]]:
                        self.tableWidget_6.setItem(
                            i, location[terminater[j]], QTableWidgetItem(actionTable[i][terminater[j]]))
                for jj in range(len(nonterminater)):
                    if GOTOtable[i][nonterminater[jj]]:
                        self.tableWidget_6.setItem(i, location[nonterminater[jj]], QTableWidgetItem(
                            str(GOTOtable[i][nonterminater[jj]])))

    def wenj(self, MainWindow):
        global IsOpen
        if os.path.exists(self.wenben.text()) is False:
            QMessageBox.critical(MainWindow, "错误", "打开文件失败！",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if self.la1.text() == '':
            QMessageBox.critical(MainWindow, "错误", "请输入分析串",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        if IsOpen is False:
            QMessageBox.critical(MainWindow, "错误", "打开文件失败",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        result = main.StackSolve(self.la1.text(), self.Lr)
        if result == []:
            QMessageBox.critical(MainWindow, "错误", "无法分析",
                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            return
        self.tableWidget_7.setColumnCount(5)
        self.tableWidget_7.setRowCount(len(result))
        for i in range(len(result)):
            self.tableWidget_7.setItem(i, 0, QTableWidgetItem(str(result[i][0])))
            self.tableWidget_7.setItem(i, 1, QTableWidgetItem(result[i][1]))
            self.tableWidget_7.setItem(i, 2, QTableWidgetItem(result[i][2]))
            self.tableWidget_7.setItem(i, 3, QTableWidgetItem(result[i][3]))
            self.tableWidget_7.setItem(i, 4, QTableWidgetItem(result[i][4]))


def go():
    app = QtWidgets.QApplication(sys.argv)
    aw = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    aw.setupUi(w)
    w.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    go()
