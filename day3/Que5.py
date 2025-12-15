def greet(name="Student"):
    print("Hello", name)

greet()
greet("Akshata")


def student_info(name, age, course):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

student_info(age=20, course="IoT", name="Akshata ")


def square(n):
    return n * n

def calculate(func, value):
    result = func(value)
    print("Result:", result)

calculate(square, 5)


def add(a, b=10):
    return a + b

def show_result(operation, x):
    print("Result:", operation(x))

show_result(add, 5)

