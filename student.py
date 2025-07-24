class Student:
    def __init__(self, name, age, grade, course):
        self.name = name
        self.age = age
        self.grade = grade
        self.course = course

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

    def display_info(self):
        print("=== Student Details ===")
        print(f"Name  : {self.name}")
        print(f"Age   : {self.age}")
        print(f"Grade : {self.grade}")
        print(f"Course: {self.course}")

# Creating an object
student1 = Student("Alice", 20, "A", "Computer Science")

# Using the methods
print(student1.introduce())
student1.display_info()


#output 

My name is Alice and I am 20 years old.
=== Student Details ===
Name  : Alice
Age   : 20
Grade : A
Course: Computer Science
