# dict = {'taha': 20, 'ali': 19}
# dict = {'taha': 20, 'ali': 19, 'ali': 50}

# print(dict)
# print(dict['ali'])

# ////////////////////////////////////

# set = {'taha', 'ali'}
# print(set)
# print('         ')

# set_1 = {1,2,3,2,3,'taha'}
# print(set_1)
# set_1.add('zare')
# set_1.update([9,10,12])
# set_1.remove(2)
# print(10 in set_1)
# print(set_1)


# set_one = {1,2,3}
# set_two = {1,2,3}
# set_3 = set_one.union(set_two)
# print(set_3)

# set_one = {1,2,3,'a'}
# set_two = {1,2,3}
# set_3 = set_one.difference(set_two)
# print(set_3)

# dic_1 = {}
# dic_1['age'] = 20
# dic_1['name'] = 'taha'
# # del dic_1['age']

# list_key = list(dic_1.keys())
# list_values = list(dic_1.values())
# print(list_key)
# print(list_values)
# list_one = [x for x in nums if x < 7]
# list_two = list(x for x in nums if x <= 3)
# print(nums)
from ctypes.wintypes import WORD


nums_2 = [1, 3, 5, 7, 9]

words = ['I','L','O','V','E']
sent = ' '.join(words)
print(sent)