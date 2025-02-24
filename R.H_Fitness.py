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
        self.template_tab_widget = self.findChild(QtWidgets.QTabWidget, "template_tab_wdgt") #AI
        self.shoulders_button = self.findChild(QPushButton, "shoulders_btn") #AI

        self.shoulders_button.clicked.connect(self.load_shoulders) #AI



    def load_shoulders(self):
        try:
            # Load shoulders tab UI as a QWidget
            shoulders_tab = QWidget()
            uic.loadUi("shoulders_widget.ui", shoulders_tab)

            # Ensure template_tab_widget exists
            if self.template_tab_widget is None:
                print("Error: self.template_tab_widget is None")
                return

            # Get parent widget of the current tab
            parent_widget = self.template_tab_widget.parentWidget()
            if parent_widget is None:
                print("Error: Template tab widget has no parent!")
                return

            # Get or create the parent layout
            parent_layout = parent_widget.layout()
            if parent_layout is None:
                print("No layout found, creating a new QVBoxLayout")
                parent_layout = QtWidgets.QVBoxLayout()
                parent_widget.setLayout(parent_layout)

            # Remove and delete the old tab
            parent_layout.removeWidget(self.template_tab_widget)
            self.template_tab_widget.deleteLater()

            # Replace it with shoulders_tab
            self.template_tab_widget = shoulders_tab
            parent_layout.addWidget(self.template_tab_widget)

            print("Successfully replaced template_tab_widget with shoulders_tab")

        except Exception as e:
            print("Error loading shoulders tab:", str(e))

    #def load_shoulders(self): #AI
  #      try: #AI

    #        shoulders_window = QtWidgets.QMainWindow() #AI
     #       uic.loadUi("shoulders_tab_widget.ui", shoulders_tab) #AI
#
#
 #           shoulders_tab = shoulders_window.centralWidget()
  #          if shoulders_tab is None:
   #             print("Error: central widget is not found in shoulders_window")
    #            return
#
 #           if self.template_tab_widget is None:
  #              print("Error: self.template_tab_widget is None")
   #             return
#
 #           parent_widget = self.template_tab_widget.parentWidget()
 #           if parent_widget is None:
  #              print("Error: Template tab widget has no parent!")
   #             return
#
 #           parent_layout = parent_widget.layout()
  #          if parent_layout is None:
   #             print("No layout found, creating a new QVBoxLayout")
    ##            parent_layout = QtWidgets.QVBoxLayout()
      ##          parent_widget.setLayout(parent_layout)
#
 #           parent_layout.removeWidget(self.template_tab_widget)
  ##          self.template_tab_widget.deleteLater()
#
 #           self.template_tab_widget = shoulders_tab
    #        parent_layout.addWidget(self.template_tab_widget)
  ##          print("Successfully replaced template_tab_widget with shoulders_tab")

    #    except Exception as e:
     #       print("Error loading shoulders tab:", str(e))


            #parent_layout.removeWidget(self.template_tab_widget)
            #parent_layout.removeWidget(self.template_tab_widget)
            #self.template_tab_widget.deleteLater()
            #self.template_tab_widget = shoulders_tab
            #parent_layout.addWidget(self.template_tab_widget)

            #parent_layout = self.template_tab_widget.parentWidget().layout()  #AI
            #if parent_layout is None:  #AI
                #print("Error: Parent layout is None") #AI
                #return #AI

            # AI - Remove the existing template tab widget
            #parent_layout.removeWidget(self.template_tab_widget) #AI
            #self.template_tab_widget.deleteLater() #AI

            # Replace it with the new shoulders_tab
            #self.template_tab_widget = shoulders_tab #AI
            #parent_layout.addWidget(self.template_tab_widget) #AI

            #print("Successfully replaced template_tab_widget with shoulders_tab") #AI

        #except Exception as e:  #AI
            #print("Error loading shoulders tab:" , str(e))  #AI

            #if self.template_tab_widget is None: #AI
             #   print("Error: self.template_tab_widget is None")  #AI
              #  return  #AI

            #parent_widget = self.template_tab_widget.parentWidget()  #AI

            #if parent_widget is None:  #AI
             #   print("Error: Template tab widget has no parent!")  #AI
              #  return  #AI

        # Get the parent layout
            #parent_layout = parent_widget.layout()  #AI

        # If there's no layout, create a new one
            #if parent_layout is None:  #AI
             #   print("No layout found, creating a new QVBoxLayout")  #AI
              #  parent_layout = QtWidgets.QVBoxLayout()  #AI
               # parent_widget.setLayout(parent_layout)  #AI

            #parent_layout.removeWidget(self.template_tab_widget)  #AI
            #self.template_tab_widget.deleteLater()  #AI

        # Replace with shoulders_tab
            #self.template_tab_widget = shoulders_tab  #AI
            #parent_layout.addWidget(self.template_tab_widget)  #AI

            #print("Successfully replaced template_tab_widget with shoulders_tab")  #AI

        #except Exception as e:  #AI
         #   print("Error loading shoulders tab:", str(e))  #AI

            

import os #AI
print(os.path.exists("shoulders_tab_widget.ui")) #AI


app = QApplication(sys.argv)
window = Fitness_UI()
app.exec_()
sys.exit(app.exec_())
