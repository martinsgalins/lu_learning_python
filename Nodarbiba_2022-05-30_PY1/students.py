class Student:

    def __init__(self, name):

        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades) != 0:
            return sum(self.grades) / len(self.grades)

        return 0


bruno = Student(name='Bruno')
bruno.add_grade(7)
bruno.add_grade(7)
bruno.add_grade(7)
bruno.add_grade(7)

print(bruno.get_average_grade())
