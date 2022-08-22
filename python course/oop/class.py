class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def details(self):
        print(f'score {self.name}  is {self.score}')

# student_one = Student('taha', 12)
# print(f'{student_one.name} : {student_one.score}')
# student_one.details()

# //////////////////////////////////////////////////////////////////////////

# student_one = Student('taha', 12)
# student_two = Student('ali', 2)

# my_students = [student_one,student_two]
# print(my_students[0].name)
# my_students[1].details()

# //////////////////////////////////////////////////////////////////////////    