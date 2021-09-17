import os
term_size = os.get_terminal_size()
print('=' * term_size.columns)
#--------------------------------------------
first_name ="le"
last_name ="van phong"

full_name=first_name + " " + last_name

print(full_name.title())

print(full_name.upper())

print(full_name.lower())

# whiteSpace and tabs
print("List of language: \n\t\t python \n\t\t C++ \n\t\t Java ")

print("\"List of language: \n\t\t python \n\t\t C++ \n\t\t Java \" ".title())

#print multiline
print("""
Find a quote from a famous person you admire Print the
quote and the name of its author Your output should look something like the
following, including the quotation marks.
""")

print("""
Albert Einstein once said, “A person who never made a
mistake never tried anything new.”
""")

#strip
person_name=" le van phong   "

print(person_name.lstrip())

print(person_name.rstrip())

print(person_name.upper().strip())
