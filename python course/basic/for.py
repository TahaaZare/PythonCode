# cars = ['benz','bmw','mvm','pride','zantiya','samand']
# for car in cars[2:5] :
#     print(car)]
# import datetime
# from time import strftime
# # for i in range(0, 6):
# #     if i % 5 == 0:
# #         time.sleep(1)
# #         print('HOB')
# #     else:
# #         time.sleep(1)
# #         print(i)

# print(datetime.datetime.now())
# print('*************************')
# print(strftime("%Y/%m/%d"))
# import time
# for i in range(1, 101):
#     if i % 5 == 0:
#         break
#     else:
#         print(i)

# list of name

# names = ['ali','saeed','mina','amir reza','taha']
# for name in names:
#     if name == 'amir reza':
#         pass
#         # continue
#         # break
#     else:
#         print(name)

# students = {'taha': 18}
# for key,value in students.items():
#     # print(f'{key} : {value}')
#     print(key + " : " + str(value))

# for key in students.keys():
#     print(key)

# for value in students.values():
#     print(value)

students = {'taha': 18, 'ali': 20, 'mina': 20}
for key, value in students.items():
    if (value == 20):
        print('********************************************')
        print(f'best student in year {key} : {value}')
