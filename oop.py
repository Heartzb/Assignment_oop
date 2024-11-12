#Object Orientated Programing
#It always has classes and objects
#A class always has properties/atributes
#Objects come from class
#An object takes on the properties of a class

#syntax
# create a classes
# corhot class # classname start with a capital letter
#class  Corhot:
   # name 
    #description
    #start_date
    #end_date
    #total_student
     


#Add a contructor to the cohort class
#Add a method to the class that prints the corhort name and the total number of students
#create a new instance of the cohort class    
    


class Cohort():
    def __init__(self,name,description,start_date,end_date,total_number_of_students) :
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.total_number_of_students = total_number_of_students
   
   
    def print_info(self):
        print(f"The total number of students in {self.name} is {self.total_number_of_students}")

New_cohort = Cohort("cohort4","An intellegent class","05/08/2024","06/08/2026",60)  
New_cohort.print_info()

    
