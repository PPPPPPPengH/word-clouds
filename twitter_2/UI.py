from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from text_processing import *
from twitter import get_tweets



class main_ui(QMainWindow):
    
    def __init__(self):
        super(main_ui, self).__init__()
        self.setWindowTitle("Automatic Creation of Word Clouds")
        self.setGeometry(150,150,540,400)
        self.initUI()

    def initUI(self):
        
        #region Title label, general message
        self.label_title =QtWidgets.QLabel(self)
        self.label_title.setText("Create a word cloud by searching content on twitter!!")
        self.label_title.move(30,30)
        self.label_title.setFont(QFont('Arial',12))
        self.label_title.adjustSize()
        
    
        self.label_search = QtWidgets.QLabel(self)
        self.label_search.setText("Write the terms of search in the box below:")
        self.label_search.move(30,80)
        self.label_search.setFont(QFont('Arial',9))
        self.label_search.adjustSize()

        self.search_word=QtWidgets.QLineEdit(self)
        self.search_word.setGeometry(QtCore.QRect(30, 100, 300, 30))
        
        #endregion

        #region pick language
        self.label_filter_language = QtWidgets.QLabel(self)
        self.label_filter_language.setText("Filter by language:")
        self.label_filter_language.move(30,150)
        self.label_filter_language.setFont(QFont('Arial',9))
        self.label_filter_language.adjustSize()

        self.pick_lang = QtWidgets.QComboBox(self)
        self.pick_lang.setGeometry(QtCore.QRect(30, 170, 200, 25))
        self.pick_lang.addItem("es")
        self.pick_lang.addItem("en")
        self.pick_lang.addItem("fr")

        #endregion


        #region pickdate

        self.label_filter_date = QtWidgets.QLabel(self)
        self.label_filter_date.setText("Filter by date:")
        self.label_filter_date.move(30,220)
        self.label_filter_date.setFont(QFont('Arial',9))
        self.label_filter_date.adjustSize()

        self.box_Date = QtWidgets.QGroupBox(self)
        self.box_Date.setGeometry(QtCore.QRect(30, 240, 320, 100))
        self.box_Date.setTitle("Date")

        self.label_start = QtWidgets.QLabel(self.box_Date)
        self.label_start.setGeometry(QtCore.QRect(7, 20, 60, 15))
        self.label_start.setText("Start (dd/mm/yyyy):")
        self.label_start.setFont(QFont('Arial',8))
        self.label_start.adjustSize()

        self.day_number_start = QtWidgets.QSpinBox(self.box_Date)
        self.day_number_start.setGeometry(QtCore.QRect(150, 20, 45, 22))
        self.day_number_start.setMinimum(1)
        self.day_number_start.setMaximum(31)

        self.month_number_start = QtWidgets.QSpinBox(self.box_Date)
        self.month_number_start.setGeometry(QtCore.QRect(200, 20, 45, 22))
        self.month_number_start.setMinimum(1)
        self.month_number_start.setMaximum(12)

        self.year_number_start = QtWidgets.QSpinBox(self.box_Date)
        self.year_number_start.setGeometry(QtCore.QRect(250, 20, 50, 22))
        self.year_number_start.setMinimum(2007)
        self.year_number_start.setMaximum(2022)

        self.label_end = QtWidgets.QLabel(self.box_Date)
        self.label_end.setGeometry(QtCore.QRect(7, 60, 60, 15))
        self.label_end.setText("End (dd/mm/yyyy):")
        self.label_end.setFont(QFont('Arial',8))
        self.label_end.adjustSize()

        self.day_number_end = QtWidgets.QSpinBox(self.box_Date)
        self.day_number_end.setGeometry(QtCore.QRect(150, 60, 45, 22))
        self.day_number_end.setMinimum(1)
        self.day_number_end.setMaximum(31)

        self.month_number_end = QtWidgets.QSpinBox(self.box_Date)
        self.month_number_end.setGeometry(QtCore.QRect(200, 60, 45, 22))
        self.month_number_end.setMinimum(1)
        self.month_number_end.setMaximum(12)

        self.year_number_end = QtWidgets.QSpinBox(self.box_Date)
        self.year_number_end.setGeometry(QtCore.QRect(250, 60, 50, 22))
        self.year_number_end.setMinimum(2007)
        self.year_number_end.setMaximum(2022)

        #endregion


        #region buttons
        self.search=QtWidgets.QPushButton(self)
        self.search.setText("Create")
        self.search.move(290,360)
        self.search.clicked.connect(self.search_tweets)

        self.new=QtWidgets.QPushButton(self)
        self.new.setText("New")
        self.new.move(400,360)
        self.new.clicked.connect(self.new_search)

        #endregion
    

        #region Definition of functions


    def search_tweets(self):
        
        day_start = int(self.day_number_start.text())
        month_start = int(self.month_number_start.text())
        year_start = int(self.year_number_start.text())
        day_end = int(self.day_number_end.text())
        month_end = int(self.month_number_end.text())
        year_end = int(self.year_number_end.text())

        if compare_dates(day_start,month_start,year_start,day_end,month_end,year_end)==False:
            return False

        else:
            searched_word = str(self.search_word.text())
            searched_word = tweet_to_words(searched_word)
            
            if searched_word == "":
                return False
            else:
                dates_string = dates_to_string(day_start, month_start, year_start, day_end, month_end, year_end)
                lan = self.pick_lang.currentText()
                tweets = get_tweets(lan = lan, search = searched_word, start_time=dates_string[0], end_time=dates_string[1])[1]
                
                tweets_text(tweets, searched_word=searched_word,lan=lan)

                return True

    def new_search(self):
        self.search_word.setText("")
        self.day_number_start.setValue(1)
        self.month_number_start.setValue(1)
        self.year_number_start.setValue(2007)
        self.day_number_end.setValue(1)
        self.month_number_end.setValue(1)
        self.year_number_end.setValue(1)
        return True

    #endregion

def wordcloud():
    app = QApplication(sys.argv)
    win = main_ui()
    win.show()
    sys.exit(app.exec_())

wordcloud()