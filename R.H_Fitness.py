# Welcome to R.H Fitness !!

## These are notes for me to understand what my code is doing


## Importing the sys to allow access for item-specific parameters and functions 
import sys 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QPushButton, \
    QLabel, QFrame
from PyQt5 import uic

## Defining my class 'Fitness_UI' to inherit from QMainWindow
class Fitness_UI(QMainWindow):
    def openNewWindow(self):
        ## Method 'openNewWindow' initialises a new instance of QMainWindow and assigns it to self.window
        self.window = QtWidgets.QMainWindow()  

    ## Constructor for the class, which initialises an object's state 
    def __init__(self):

        super(Fitness_UI,self).__init__() # call constrcutor of parent class

        ##Loads the xml file and converts into readable python
        uic.loadUi("mainwindow.ui",self)  


