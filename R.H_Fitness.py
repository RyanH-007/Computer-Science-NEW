# Welcome to R.H Fitness !!

## These are notes for me to understand what my code is doing


## Importing the sys to allow access for item-specific parameters and functions 
import json
import datetime
import os
import sys 
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow,QWidget,QPushButton, \
    QLabel, QFrame, QTabWidget, QLineEdit
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
        self.heart_button.clicked.connect(self.h_h_btn_clicked)
        self.bmi_button.clicked.connect(self.bmi_btn_clicked)

        self.update_daily_quote()

        self.show()

    def update_daily_quote(self):
        file_path = "quotes.json"
        
        if not os.path.exists(file_path):
            print("Quote file not found!")
            return
        
        try:
            # Load quotes from the JSON file
            with open(file_path, "r") as file:
                quotes = json.load(file)
            
            # Get the current day of the month (1-31)
            day_of_month = datetime.datetime.now().day
            
            # Ensure there are 31 quotes in the list
            if isinstance(quotes, list) and len(quotes) >= 31:
                daily_quote = quotes[(day_of_month - 1) % 31]  # Wrap around if needed
                self.quote.setText(daily_quote)
            else:
                print("Invalid quote data format!")
        except Exception as e:
            print(f"Error loading quotes: {e}")


         ## defining the function for gym section clicked    
    def g_s_btn_clicked(self): #AI
        self.gym_window = GymSectionWindow()
        self.gym_window.show()
    

    def h_h_btn_clicked(self):
        self.heart_window = HeartHealthSectionWindow()
        self.heart_window.show()
    
    def bmi_btn_clicked(self):
        self.bmi_window = BMISectionWindow()
        self.bmi_window.show()


class BMISectionWindow(QMainWindow):
    def __init__(self):
        super(BMISectionWindow, self).__init__()
        uic.loadUi("R.H_Fitness_bmi_window.ui", self)

        self.bmi_age_line_edit = self.findChild(QLineEdit, "bmi_age_line_edit")
        self.bmi_weight_line_edit = self.findChild(QLineEdit, "bmi_weight_line_edit")
        self.bmi_height_line_edit = self.findChild(QLineEdit, "bmi_height_line_edit")

        self.save_button = self.findChild(QPushButton, "bmi_save_btn")  # Make sure the objectName in Designer is "save_button"
        self.save_button.clicked.connect(self.save_data)

    def save_data(self):
        # Gather data from the QLineEdits
        data = {
            "age": self.bmi_age_line_edit.text(),
            "weight": self.bmi_weight_line_edit.text(),
            "height": self.bmi_height_line_edit.text(),
        }

        # Write data to a JSON file
        try:
            # Define the path for the JSON file
            file_path = "bmi_data.json"
            
            # Check if the file exists; if it does, we will update it; otherwise, we'll create a new one
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    existing_data = json.load(file)
            else:
                existing_data = {}

            # Update the existing data with the new data
            existing_data.update(data)

            # Save the updated data back into the JSON file
            with open(file_path, "w") as file:
                json.dump(existing_data, file, indent=4)

            print("Data saved successfully.")

        except Exception as e:
            print(f"Error saving data: {e}")





'''class HeartHealthSectionWindow(QMainWindow):
    def __init__(self):
        super(HeartHealthSectionWindow, self).__init__()
        uic.loadUi("R.H_Fitness_h_h_window.ui", self)

        self.age_line_edit = self.findChild(QLineEdit, "age_line_edit")
        self.weight_line_edit = self.findChild(QLineEdit, "weight_line_edit")
        self.height_line_edit = self.findChild(QLineEdit, "height_line_edit")
        self.heart_rate_running_line_edit = self.findChild(QLineEdit, "heart_rate_running_line_edit")
        self.heart_rate_stationary_line_edit = self.findChild(QLineEdit, "heart_rate_stationary_line_edit")

        # Find and connect the "Save" button (you need to add this button in Qt Designer if not already present)
        self.save_button = self.findChild(QPushButton, "h_h_save_btn")  # Make sure the objectName in Designer is "save_button"
        self.save_button.clicked.connect(self.save_data)

    def save_data(self):
        # Gather data from the QLineEdits
        data = {
            "age": self.age_line_edit.text(),
            "weight": self.weight_line_edit.text(),
            "height": self.height_line_edit.text(),
            "heart_rate_running": self.heart_rate_running_line_edit.text(),
            "heart_rate_stationary": self.heart_rate_stationary_line_edit.text(),
        }

        # Write data to a JSON file
        try:
            # Define the path for the JSON file
            file_path = "heart_health_data.json"
            
            # Check if the file exists; if it does, we will update it; otherwise, we'll create a new one
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    existing_data = json.load(file)
            else:
                existing_data = {}

            # Update the existing data with the new data
            existing_data.update(data)

            # Save the updated data back into the JSON file
            with open(file_path, "w") as file:
                json.dump(existing_data, file, indent=4)

            print("Data saved successfully.")

        except Exception as e:
            print(f"Error saving data: {e}")


    def load_heart_health_calculation():
        """Loads the predefined healthy heart rate ranges from a JSON file."""
        file_path = "heart_health_calculation.json"
        if not os.path.exists(file_path):
            print("Healthy heart data file not found!")
            return None
        
        with open(file_path, "r") as file:
            return json.load(file)

    def load_average_weight_data():
        """Loads the predefined average weight ranges for each height."""
        file_path = "average_weight_data.json"
        if not os.path.exists(file_path):
            print("Average weight data file not found!")
            return None
        
        with open(file_path, "r") as file:
            return json.load(file)

    def evaluate_hear_health_calculation(user_data):
        """Evaluates heart health based on user inputs and predefined healthy ranges."""
        healthy_data = load_heart_health_calculation()
        weight_data = load_average_weight_data()
        if not healthy_data or not weight_data:
            return "Cannot evaluate heart health. Missing reference data."
        
        h_h_age = int(user_data["age"])
        h_h_weight = float(user_data["weight"])
        h_h_height = float(user_data["height"])
        h_h_bpm_rest = int(user_data["heart_rate_stationary"])
        h_h_bpm_run = int(user_data["heart_rate_running"])
        
        # Find the appropriate age category
        for category in healthy_data["age_groups"]:
            if category["min_age"] <= age <= category["max_age"]:
                bpm_rest_range = category["bpm_rest"]
                bpm_run_range = category["bpm_run"]
                break
        else:
            return "No reference data available for your age group."
        
        # Evaluate heart rate
        is_healthy_rest = bpm_rest_range[0] <= h_h_bpm_rest <= bpm_rest_range[1]
        is_healthy_run = bpm_run_range[0] <= h_h_bpm_run <= bpm_run_range[1]
        
        # Check for BMI range if needed (optional for deeper analysis)
        bmi = h_h_weight / ((h_h_height / 100) ** 2)  # Convert height to meters
        
        # Check if weight is within the average range for the given height
        if str(int(h_h_height)) in weight_data:
            avg_weight_range = weight_data[str(int(h_h_height))]
            is_weight_healthy = avg_weight_range[0] <= h_h_weight <= avg_weight_range[1]
        else:
            is_weight_healthy = True  # Assume healthy if no data is available
        
        health_status = ""
        if is_healthy_rest and is_healthy_run:
            health_status = "Your heart rate is within the healthy range for your age group."
        else:
            health_status = "Your heart rate is outside the healthy range. There are many factors that could contribute to this."
            if not is_weight_healthy:
                health_status += " One possible factor is your weight, which is outside the average range for your height."
        
        return f"Heart Health Evaluation:\n- Resting BPM: {h_h_bpm_rest} (Healthy: {is_healthy_rest})\n- Running BPM: {h_h_bpm_run} (Healthy: {is_healthy_run})\n- BMI: {bmi:.2f}\n- Weight Status: {'Healthy' if is_weight_healthy else 'Outside Average'}\n{health_status}"

    # Example usage (assuming user_data is gathered from your GUI inputs)
    user_data = {
        "age": "25",
        "weight": "90",
        "height": "160",
        "heart_rate_running": "150",
        "heart_rate_stationary": "90"
    }

    print(evaluate_heart_health_calculation(user_data))


'''

class HeartHealthSectionWindow(QMainWindow):
    def __init__(self):
        super(HeartHealthSectionWindow, self).__init__()
        uic.loadUi("R.H_Fitness_h_h_window.ui", self)

        self.age_line_edit = self.findChild(QLineEdit, "age_line_edit")
        self.weight_line_edit = self.findChild(QLineEdit, "weight_line_edit")
        self.height_line_edit = self.findChild(QLineEdit, "height_line_edit")
        self.heart_rate_running_line_edit = self.findChild(QLineEdit, "heart_rate_running_line_edit")
        self.heart_rate_stationary_line_edit = self.findChild(QLineEdit, "heart_rate_stationary_line_edit")

        self.save_button = self.findChild(QPushButton, "h_h_save_btn")
        self.save_button.clicked.connect(self.save_data)

    def save_data(self):
        data = {
            "age": self.age_line_edit.text(),
            "weight": self.weight_line_edit.text(),
            "height": self.height_line_edit.text(),
            "heart_rate_running": self.heart_rate_running_line_edit.text(),
            "heart_rate_stationary": self.heart_rate_stationary_line_edit.text(),
        }

        try:
            file_path = "heart_health_data.json"
            if os.path.exists(file_path):
                with open(file_path, "r") as file:
                    existing_data = json.load(file)
            else:
                existing_data = {}

            existing_data.update(data)

            with open(file_path, "w") as file:
                json.dump(existing_data, file, indent=4)

            print("Data saved successfully.")

        except Exception as e:
            print(f"Error saving data: {e}")

    def load_heart_health_calculation(self):
        """Loads the predefined healthy heart rate ranges from a JSON file."""
        file_path = "heart_health_calculation.json"
        if not os.path.exists(file_path):
            print("Healthy heart data file not found!")
            return None
        
        with open(file_path, "r") as file:
            return json.load(file)

    def load_average_weight_data(self):
        """Loads the predefined average weight ranges for each height."""
        file_path = "average_weight_data.json"
        if not os.path.exists(file_path):
            print("Average weight data file not found!")
            return None
        
        with open(file_path, "r") as file:
            return json.load(file)

    def evaluate_heart_health_calculation(self, user_data):
        """Evaluates heart health based on user inputs and predefined healthy ranges."""
        healthy_data = self.load_heart_health_calculation()
        weight_data = self.load_average_weight_data()
        if not healthy_data or not weight_data:
            return "Cannot evaluate heart health. Missing reference data."
        
        h_h_age = int(user_data["age"])
        h_h_weight = float(user_data["weight"])
        h_h_height = float(user_data["height"])
        h_h_bpm_rest = int(user_data["heart_rate_stationary"])
        h_h_bpm_run = int(user_data["heart_rate_running"])
        
        for category in healthy_data["age_groups"]:
            if category["min_age"] <= h_h_age <= category["max_age"]:
                bpm_rest_range = category["bpm_rest"]
                bpm_run_range = category["bpm_run"]
                break
        else:
            return "No reference data available for your age group."
        
        is_healthy_rest = bpm_rest_range[0] <= h_h_bpm_rest <= bpm_rest_range[1]
        is_healthy_run = bpm_run_range[0] <= h_h_bpm_run <= bpm_run_range[1]
        
        bmi = h_h_weight / ((h_h_height / 100) ** 2)  

        if str(int(h_h_height)) in weight_data:
            avg_weight_range = weight_data[str(int(h_h_height))]
            is_weight_healthy = avg_weight_range[0] <= h_h_weight <= avg_weight_range[1]
        else:
            is_weight_healthy = True  
        
        health_status = ""
        if is_healthy_rest and is_healthy_run:
            health_status = "Your heart rate is within the healthy range for your age group."
        else:
            health_status = "Your heart rate is outside the healthy range. There are many factors that could contribute to this."
            if not is_weight_healthy:
                health_status += " One possible factor is your weight, which is outside the average range for your height."
        
        return f"Heart Health Evaluation:\n- Resting BPM: {h_h_bpm_rest} (Healthy: {is_healthy_rest})\n- Running BPM: {h_h_bpm_run} (Healthy: {is_healthy_run})\n- BMI: {bmi:.2f}\n- Weight Status: {'Healthy' if is_weight_healthy else 'Outside Average'}\n{health_status}"


# Example of how to use it inside the class:
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HeartHealthSectionWindow()

    user_data = {
        "age": "25",
        "weight": "90",
        "height": "160",
        "heart_rate_running": "150",
        "heart_rate_stationary": "90"
    }

    print(window.evaluate_heart_health_calculation(user_data))

    window.show()
    app.exec_()



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
        self.calfs_button = self.findChild(QPushButton, "calfs_btn")
        self.upper_back_button = self.findChild(QPushButton, "upper_back_btn")
        self.lats_button = self.findChild(QPushButton, "lats_btn")
        self.glutes_button = self.findChild(QPushButton, "glutes_btn")
        self.hamstrings_button = self.findChild(QPushButton, "hamstrings_btn")
    



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
        self.lower_back_button.clicked.connect(lambda: self.load_tab("lower_back_widget.ui", "lower back"))
        self.calfs_button.clicked.connect(lambda: self.load_tab("calfs_widget.ui", "calfs"))
        self.upper_back_button.clicked.connect(lambda: self.load_tab("upper_back_widget.ui", "upper back"))
        self.lats_button.clicked.connect(lambda: self.load_tab("lats_widget.ui", "lats"))
        self.glutes_button.clicked.connect(lambda: self.load_tab("glutes_widget.ui", "glutes"))
        self.hamstrings_button.clicked.connect(lambda: self.load_tab("hamstrings_widget.ui", "hamstrings")) 
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
