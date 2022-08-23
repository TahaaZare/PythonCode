from math import gamma


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


class Fish:
    def swiming(self):
        print('swimming')

    def eat(self):
        print('eating')


class Game:
    def __init__(self, name: str, year: int):
        self.name = name
        self.year = year

    def Start(self):
        print(f'{self.name} has started Game!')

    def Stop(self):
        print(f'{self.name} , has Stoped the Game !')


game = Game('RDD2', 2003)
game.Start()
game.Stop()
