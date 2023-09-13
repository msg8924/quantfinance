from Person import Person
class Student(Person):
    def __init__(self, first_name, last_name, age, major):
        super().__init__(first_name, last_name,age)
        self.major = major
    def print(self):
        print("Name is " + self.first_name + " " + self.last_name + " ,age is " + str(self.age) + " and major is " + self.major)

if __name__ == '__main__':
    student = Student("Avi", "Gill", 41, "Data Science")
    student.print()