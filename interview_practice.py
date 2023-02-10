class Person():
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def __str__(self):
        return f"{self.name},{self.age},{self.gender}"

class Student(Person):
    studentId = 1
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.rollNo = Student.studentId
        Student.studentId += 1
    
    def __str__(self):
       return super().__str__() + f",{self.rollNo}"

newPerson = Person('gautam',23,'M')
print(newPerson)

newStudent = Student('gaurav', 18, 'M')
print(newStudent)