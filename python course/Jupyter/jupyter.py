# number_one  = int(input('enter a number : '))
# number_two  = int(input('enter another number : '))
# result = number_one + number_two
# #print(result)  # Inputs

# text = """this is a text. is it U ? yes its ME

# When i Was a child.
# & ?
# """
# with open('TestFilePython.txt', 'a') as file:
#     file.write(text)
#     file.close()

# fullname = 'Taha Zare'
# with open('TestFilePython1.txt', 'a') as file:
#     file.write(fullname)
#     file.close()

# try:
#     with open('TestFilePython2.txt', 'r') as file:
#         UserFullname = file.read()
#         print(UserFullname)

# except IOError:
#     print('ERORR')


# ////////////////////////////////////////////////////////////////////

# import pickle

# exmaple_Dict = {'a': 12, 'b': 45, 'c': 5}
# pickel_out = open('PickleDict', 'wb')  # //wb = write binary
# pickle.dump(exmaple_Dict, pickel_out)
# pickel_out.close()

# pickle_in = open('PickleDict', 'rb')
# exm = pickle.load(pickle_in)
# print(exm)

def sumofmany(nums):
    total = 0
    for num in nums:
        total += num
    return total

# print(sumofmany([1,2,3,4]))
# print(sum([1,2,3,4,1,2,3,1,2,3,1,3,4]))

def JustPrint(*args):
    for arg in args:
        print(arg)

# JustPrint('hello','welcome','to','python')        
JustPrint('hello welcome to python')        