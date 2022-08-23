import re

text = """101 COM    Computers
205 MAT   Mahamtics
189 ENG   English"""

farsi_text = """در حال تماشای 13 سالگی برنامه کمدی هستید"""
farsi_text_2 = """21 فروردین 1401 """
# pattern = '[ا-ی]{3,}'
# pattern = r'\d{2,4}' 
# pattern = 'فروردی?ن' 
strings = 'لطفا با ایمیل من tahaazre@gmail.com تماس بگیرید.'
print(re.findall(r'\w+@[A-Za-z]+\.[A-Za-z]+',strings))

# pattern = '[A-Z]{3}'
# pattern = '[A-Z]{4}'
# pattern = '[A-Z]{1,}'
# list_obj = re.findall(pattern,text)
# print(list_obj)

# pattern = '[A-Za-z]{4}'
# list_obj = re.findall(pattern,text)
# print(list_obj)

# pattern = r'\s+'
# regex_one = re.compile(pattern)
# list_obj = regex_one.split(text)
# print(list_obj)

# pattern = r'\d+'
# match_obj = re.search(pattern,text)
# # print(match_obj)
# print(match_obj.start())
# print(match_obj.end())
# print(match_obj.span())
# print(match_obj.group())


# pattern = r'\d+'
# match_obj = re.match(pattern,text)
# # print(match_obj)
# print(match_obj.start())
# print(match_obj.end())
# print(match_obj.span())
# print(match_obj.group(0))

# pattern = r'\d+'
# match_obj = re.match(pattern,'110 rohn')
# # print(match_obj)
# print(match_obj.start())
# print(match_obj.end())
# print(match_obj.span())
# print(match_obj.group(0))

# pattern = '[a-z]'
# match_obj = re.findall(pattern,text)
# print(match_obj)

# /////////////////////////////////////////////////////////////
# text = 'W!@isdmi&|C P@:an,@da'
# list_one = re.split("['?@,:\s\'|&]+" , text)
# print(list_one)

# text = 'W!@isdmi&|C P@:an,@da'
# list_one_('', text)
# print(list_one)