class Student:

    def __init__(self, name, __age, grades):
        self.name = name
        self.__age = __age
        self.grades = grades

    
    def get_age(self):
        return self.__age


    def __str__(self):
        print('in str')
        return (f"Student name is : {self.name}, grades are {self.grades} and age is {self.__age} ")    
    
    def __repr__(self):
        print('in repr')
        return (f"Student name is : {self.name}, grades are {self.grades} and age is {self.__age} ")    


student = Student("Rakesh", "20", [90,80,70,80])
print(student.grades)
print(student.get_age())
#print(student.avg())

print(student)
