# Welcome to R.H Fitness !!

## These are notes for me to understand what my code is doing


## Importing the sys to allow access for item-specific parameters and functions 
import sys 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QPushButton, \
    QLabel, QFrame, QTabWidget
from PyQt5 import uic

## Defining my class 'Fitness_UI' to inherit from QMainWindow
class Fitness_UI(QMainWindow):
    def openNewWindow(self):
        ## Method 'openNewWindow' initialises a new instance of QMainWindow and assigns it to self.window
        self.window = QtWidgets.QMainWindow()  

    ## Constructor for the class, which initialises an object's state 
    def __init__(self):

        super(Fitness_UI,self).__init__() # call constrcutor of parent class         #AI

        ##Loads the xml file and converts into readable python
        uic.loadUi("R.H_Fitness_mainwindow.ui",self)  
        
        self.title = self.findChild(QLabel,"title_lbl")
        self.quote = self.findChild(QLabel,"quote_lbl")
        self.gym_frame = self.findChild(QFrame,"g_s_frame")
        self.heart_frame = self.findChild(QFrame,"h_h_frame")
        self.bmi_frame = self.findChild(QFrame,"bmi_frame")
        self.gym_title = self.findChild(QLabel,"g_s_title_lbl")
        self.heart_title = self.findChild(QLabel,"h_h_title_lbl")
        self.bmi_title = self.findChild(QLabel,"bmi_title_lbl")
        self.gym_button = self.findChild(QPushButton, "g_s_btn")
        self.heart_button = self.findChild(QPushButton, "h_h_btn")
        self.bmi_button = self.findChild(QPushButton, "bmi_btn")
        
       
        
               ##  setting event handlers

        self.gym_button.clicked.connect(self.g_s_btn_clicked)
        #self.heart_button.clicked.connect(self.h_h_btn_clicked)
        #self.bmi_button.clicked.connect(self.bmi_btn_clicked)
       
        
        self.show()

    ## defining the function for gym section clicked    
    def g_s_btn_clicked(self): #AI
        uic.loadUi("R.H_Fitness_g_s_window.ui",self) #AI

        self.g_s_tab = self.findChild(QTabWidget, "g_s_tab_widget") #AI
        self.template_tab_widget = self.findChild(QTabWidget, "template_tab_wdgt") #AI
        self.shoulders_button = self.findChild(QPushButton, "shoulders_btn") #AI

        self.shoulders_button.clicked.connect(self.load_shoulders) #AI


# this whole func is ai, figure out what it did 
   
    def load_shoulders(self):
        try:
            # Load shoulders tab UI as a QWidget
            shoulders_tab = QWidget()
            uic.loadUi("shoulders_widget.ui", shoulders_tab)

            # Ensure that template_tab_widget exists and is a QTabWidget
            if not isinstance(self.template_tab_widget, QTabWidget):
                print("Error: template_tab_widget is not a QTabWidget!")
                return

            # Get the index of the current tab (assuming it's the one to replace)
            current_index = self.template_tab_widget.currentIndex()

            # If there are no tabs, just add the shoulders tab
            if current_index == -1:
                self.template_tab_widget.addTab(shoulders_tab, "Shoulders")
            else:
                # Replace the current tab with the shoulders tab
                self.template_tab_widget.removeTab(current_index)
                self.template_tab_widget.insertTab(current_index, shoulders_tab,"Shoulders")

            # Set focus to the new tab
            self.template_tab_widget.setCurrentIndex(current_index)

            print("Successfully replaced the template tab with shoulders tab")

        except Exception as e:
            print("Error loading shoulders tab:", str(e))



import os #AI
print(os.path.exists("shoulders_tab_widget.ui")) #AI


app = QApplication(sys.argv)
window = Fitness_UI()
app.exec_()
sys.exit(app.exec_())
