class Student:

    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def avg(self):
        return sum(self.grades)/len(self.grades)

    def __str__(self):
        print('in str')
        return (f"Student name is : {self.name}, grades are {self.grades} and age is {self.age} ")    
    
    def __repr__(self):
        print('in repr')
        return (f"Student name is : {self.name}, grades are {self.grades} and age is {self.age} ")    


student = Student("Rakesh", "20", [90,80,70,80])
print(student.avg())

print(student)
