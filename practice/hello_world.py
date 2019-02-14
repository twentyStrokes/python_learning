print("Hello Python world!")

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

name = "ada lovelace"
print(name.title())

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("Hello, " + full_name.title() + "!")

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python '
print(favorite_language)
print(favorite_language.rstrip())

message = "One of Python's strengths is its diverse community."
print(message)
# SyntaxError: invalid syntax
# message = 'One of Python's strengths is its diverse community'
# print(message)

age = 23
# TypeError: can only concatenate str (not "int") to str
# message = "Happy " + age + "rd Birthday!"
message = "Happy " + str(age) + "rd Birthday!"
print(message)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[3])
# python 
print(bicycles[-2])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

# 排序P40






