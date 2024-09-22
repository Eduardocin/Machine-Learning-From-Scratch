# static methods : belongs to a class rather tan any object from a class.
# best for utility functions that do not need acess to the class data.

class Employee:
    #class constructor
    def __init__ (self, name, position):
        # instance attributes
        self.name = name
        self.position = position
    
    def get(self):
        return f"{self.name} = {self.position}"
    
    # static method
    @staticmethod
    def is_full_time(position):
        return position == "Full-time"
    
    
# creating objects

employee1 = Employee("John Doe", "Full-time")
employee2 = Employee("Jane Smith", "Part-time")

# accessing instance attributes

print(employee1.get())
print(employee2.get())

# calling static method dont need to usa a instance of the class

print(Employee.is_full_time("Full-time"))
print(Employee.is_full_time("Part-time"))

print(Employee.get(employee1))