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
        self.gym_window = GymSectionWindow()
        self.gym_window.show()
        
        
class GymSectionWindow(QMainWindow):
    def __init__(self):
        super(GymSectionWindow, self).__init__()
        uic.loadUi("R.H_Fitness_g_s_window.ui", self)

        self.g_s_tab = self.findChild(QTabWidget, "g_s_tab_widget") #AI
        self.template_tab_widget = self.findChild(QTabWidget, "template_tab_wdgt") #AI
        self.shoulders_button = self.findChild(QPushButton, "shoulders_btn") #AI
        self.biceps_button = self.findChild(QPushButton, "biceps_btn")
        self.forearms_button = self.findChild(QPushButton, "forearms_btn")
        self.hand_grip_button = self.findChild(QPushButton, "hands_btn")
        self.chest_button = self.findChild(QPushButton, "chest_btn")
        self.abdominals_button = self.findChild(QPushButton, "abs_btn")
        self.abductors_button = self.findChild(QPushButton, "abductors_btn")
        self.quadriceps_button = self.findChild(QPushButton, "quads_btn")
        self.traps_button = self.findChild(QPushButton, "traps_btn")
        self.triceps_button = self.findChild(QPushButton, "triceps_btn")
        self.lower_back_button = self.findChild(QPushButton, "lower_back_btn")
        self.calves_button = self.findChild(QPushButton, "calves_btn")
        self.upper_back_button = self.findChild(QPushButton, "upper_back_btn")
        self.lats_button = self.findChild(QPushButton, "lats_btn")
        self.glutes_button = self.findChild(QPushButton, "glutes_btn")
        self.hamstrings_button = self.findChild(QPushButton, "hamstring_btn")



        self.shoulders_button.clicked.connect(lambda: self.load_tab("shoulders_widget.ui", "Shoulders"))
        self.biceps_button.clicked.connect(lambda: self.load_tab("biceps_widget.ui", "biceps"))
        self.forearms_button.clicked.connect(lambda: self.load_tab("forearms_widget.ui", "forearms"))
        self.hand_grip_button.clicked.connect(lambda: self.load_tab("hand_grip_widget.ui", "hand_grip"))
        self.chest_button.clicked.connect(lambda: self.load_tab("chest_widget.ui", "chest"))
        self.abdominals_button.clicked.connect(lambda: self.load_tab("abs_widget.ui", "abs"))
        self.abductors_button.clicked.connect(lambda: self.load_tab("abductor_widget.ui", "abductors"))
        self.quadriceps_button.clicked.connect(lambda: self.load_tab("quads_widget.ui", "quads"))
        self.traps_button.clicked.connect(lambda: self.load_tab("traps_widget.ui", "traps"))
        self.triceps_button.clicked.connect(lambda: self.load_tab("triceps_widget.ui", "triceps"))
        # Example for additional buttons:
    
    
        
    

# this whole func is ai, figure out what it did 

    def load_tab(self, ui_filename, tab_name):
        try:
            # Load the requested tab UI as a QWidget
            new_tab = QWidget()
            uic.loadUi(ui_filename, new_tab)

            # Ensure that template_tab_widget exists and is a QTabWidget
            if not isinstance(self.template_tab_widget, QTabWidget):
                print("Error: template_tab_widget is not a QTabWidget!")
                return

            # Get the index of the current tab (assuming it's the one to replace)
            current_index = self.template_tab_widget.currentIndex()

            # If there are no tabs, just add the new tab
            if current_index == -1:
                self.template_tab_widget.addTab(new_tab, tab_name)
                self.template_tab_widget.setCurrentIndex(0)  # Focus on the new tab
            else:
                # Replace the current tab with the new tab
                self.template_tab_widget.removeTab(current_index)
                self.template_tab_widget.insertTab(current_index, new_tab, tab_name)
                self.template_tab_widget.setCurrentIndex(current_index)  # Keep focus on the new tab

        except Exception as e:
            print(f"Error loading {tab_name} tab:", str(e))


import os #AI
print(os.path.exists("shoulders_tab_widget.ui")) #AI


app = QApplication(sys.argv)
window = Fitness_UI()
app.exec_()
sys.exit(app.exec_())
