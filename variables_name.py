'''
❗ Tên biến chấp nhận 
	chữ cái in hoa (A-Z) hoặc in thường (a-z)
	chữ số (0-9)
	dấu gạch dưới(underscore) '_'
------------------------------
❗ Quy tắc đặt tên: 
	i.   Bắt đầu bằng chữ cái (A-Z),(a-z) hoặc dấu gạch dưới(underscore) '_', 
	ii.  Không được phép bắt đầu bằng số
	iii. Khoảng trắng (Space ) không được phép xuất hiện
	iv.  Không được đặt trùng với PYTHON KEYWORD, hoặc tên hàm
	v.   Đặt tên nên ngắn mà có ý nghĩa, nhìn vào tên có thể biết được chức năng và mục đích của nó
			full_name (chỉ toàn bộ tên gồm first_name và last_name)
	vi.  Lưu ý khi sử dụng O và l thường nhìn nhầm thành số 0 và 1


Nên đặt tên biến bằng chữ thường ? 
------------------------------
❗ Ví dụ: 
	= là phép gán (assign)

	lvphong_01 = "le van phong"

	_python_book = 'the art of programming language'

	age = 23

❌ví dụ tên biến không hợp lệ 

	$dollar = 33

	_underscore^2 = '=='

	2_million = 2*(10**6)  # 2.000.000
------------------------------
2.

Trong bài toán tính tổng thì tổng cần tính nếu không có gì đặc biệt nên đặt ngắn gọn là  
	sum

Ví dụ trong bài toán đếm số lượng sinh viên tốt nghiệp

	number_of_graduate_students = 500
	
Trong các cách đặt tên biến sau, cách đặt tên nào hợp lệ:
	• numberofcollegegraduates 

	• NUMBEROFCOLLEGEGRADUATES
		Tên hằng số đặc biệt, viết hoa hết và cách nhau bởi dấu gạch dưới DISCOUNT_PERCENT, LIMIT_RATE, GRAVITY_CONSTANT

	• numberOfCollegeGraduates 
		#Camel Case: từ đầu tiên viết thường, các từ tiếp theo viết hoa chữ cái đầu
		Tên hàm và phương thức sử dụng camelCase, ví dụ getUser, getCategory…

	• NumberOfCollegeGraduates  
		#Pascal Case: viết hoa tất cả các chữ cái đầu
		Tên lớp đặt theo PascalCase, ví dụ: UserClass, CategoryClass…

	• number_of_college_graduates 
		#Snake_case hay còn được gọi là quy tắc Underscore case
		sử dụng dấu gạch chân giữa các từ, tất cả các từ đều viết thường
		dùng để đặt tên biến, tên hàm và đôi khi cả tên tập tin trên máy tính.

'''

import os
term_size = os.get_terminal_size()

python_intro ="""Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner
tutorials reference it). Fun is a great motivator, and since you’ll be able to build prototypes and tools quickly with Python,
many find coding in Python a satisfying experience. Thus, Python has gained popularity for being a beginner-friendly
language, and it has replaced Java as the most popular introductory language at Top U.S. Universities.
"""
print(python_intro)
print('=' * term_size.columns)
# check times of appear
list_checked_words = ['Python', 'contains', 'experience', 'difficult']

for checked_word in list_checked_words:
	number_of_checked_word = (python_intro.count(checked_word))
	if number_of_checked_word == 0:
		print("\t"+ checked_word + " is not appear in this above paragraph\n")
	else:
		print("\t"+ checked_word + " is appear "+ str(number_of_checked_word)+" times in this above paragraph\n")

print('=' * term_size.columns)
# count the words of this above paragraph

words_of_paragraph = python_intro.split()
number_words = len(words_of_paragraph)

print("This above paragraph has " + str(number_words) + " words!")
print('=' * term_size.columns)

# 1
first_sentence = """"
Python was designed to be easy to understand and fun to use (its name came from Monty Python so a lot of its beginner
tutorials reference it).
"""
print(first_sentence.upper())

print('=' * term_size.columns)

#2

sentences = python_intro.split(".")
print(sentences[0].upper())
