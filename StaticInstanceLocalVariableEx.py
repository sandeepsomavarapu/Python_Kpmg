class Student:
    schoolname="HPS" #static variable
    def __init__(self,name): #local variable
        print("param constructor")
        self.name=name  #instance  variable
    def display(self):
        print(self.name," ",Student.schoolname)
student= Student("mahesh")
student1= Student("sandeep")
student.display()
student1.display()
print()
print(Student.schoolname)

#instance,static,local