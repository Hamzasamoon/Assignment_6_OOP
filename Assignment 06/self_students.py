class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"Name: {self.name} Mark: {self.marks}")

s1 = Student("Hamza", 73)
print(s1.name)
print(s1.marks)

s1.display()