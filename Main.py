print("I am new to python script")


def my_function():
    print("This is my function")
    print("Second string")

my_function()


def my_function(str1, str2):
    print(str1)
    print(str2)

my_function("This is argument1", "This is argument2")


def my_function(name = "someone", age = "unknown"):
    print("my name is",name,"my age is",age)

my_function("Nick","35")




def do_math(num1, num2):
    return num1 + num2

math1 = do_math(7,8)
math2 = do_math(20,30)

print("first sum is",math1, "second sum is",math2)




check = "Pizza"

if check == False:
    print("It is false")
elif check =="Pizza":
     print("Yummm, Pizza")
elif check == "Yo":
     print("Hello")
else:
     print("It is actually equal to true")