class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def print(self):
        print("Name is " + self.first_name + " " +  self.last_name + " and age is " + str(self.age))

if __name__ == '__main__':
    person = Person("Avi", "Gill", 41)
    person.print()