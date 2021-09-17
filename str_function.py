import this
import os
term_size = os.get_terminal_size()
print('=' * term_size.columns)

age=23
message = "Happy "+ str(age)+"rd Birthday!"

print(message)

### gán một paragraph nhiều dòng vào biến, khi in ra sẽ in đúng định dạng mà ta muốn

multiline_paragraph = """
In Python, the hash mark (#) indicates a comment. 
Anything following a hash mark in your code is ignored by the Python interpreter.
"""
print(multiline_paragraph) 