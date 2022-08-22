# dict = {'taha': 20, 'ali': 19, 'sepehr': 20}
# for key, value in dict.items():
#     if (value == 20):
#         print(f'hi {key}')

name = {'taha': 0, 'ali': 19, 'sepehr': 0}
def GetBestStudents(students):
    best_list = []
    for key, value in students.items():
        if (value == 20):
            best_list.append(key)
    if len(best_list) == 0:
        return 'no best students !'
    else:
        return best_list
    # return best_list
print(GetBestStudents(name))
# if len(GetBestStudents(name)) != 0:
#     print(GetBestStudents(name))
# else:
#     print('no best students')

