'''
practicing dictionaries and using other data structure - such as Tuples, Arrays, Objects, etc.

dictionaries are made of key value pairs
e.g data = {
    "1: one"
    "2: two"
} 

'''


# create a basic dictionary to store student test information by subject





student_information = {

    "student_1":  {"Maths: 65%", "C.S: 98%", "Geography: 80%"},

    "student_2":  {"Maths: 35%", "C.S: 43%", "Geography: 60%"},

    "student_3":  {"Maths: 67%", "C.S: 58%", "Geography: 57%"}

}


# create attricbute ' charm ' 
print(student_information["student_1"])


student_scores = {

    "Ryan": {

        "scores": {
                "maths": ["75%"],
                "geog": ["89%"],
                "C.S": ["54%"]

        } 
    }

}



# ---------------- SIR WILL GIVE US A QUESTION LIKE THIS IN TEST ----------------------------

# lets create a list for student objects

student_objects = []

class student():

    def __innit__(self, pname, pintelligence):
        self.name = pname
        self.pintelligence = pintelligence
    
    #end def

    def get_intelligence(self):
        return self.pintelligence
    
    #end def

#end class

fred = student( pname = "fred", pintelligence = 99)

# add to list
student_objects.append(fred)

sid = student( pname = "sid", pintelligence = 0)
student_objects.append(sid)

# get data about fred's intelligence from object list

#print(student_objects[0].get_intelligence())
print(student_objects[0].name)
