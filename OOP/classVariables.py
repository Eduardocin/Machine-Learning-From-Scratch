class Student:
    """
        class variables share data among all instances of the class
    """
    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age= None):
        self.name = name
        self.age = age if age is not None else "Unknown"
        Student.num_students += 1    
    


print(Student.num_students)
student1 =  Student("Spongebob", 20)
student2 = Student("Patrick", 25)


print(f"{student1.name} and {student2.name}")

print(Student.num_students)