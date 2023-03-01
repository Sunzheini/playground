x = 'print(55)'
eval(x)


# Perimeter of Square
def calculatePerimeter(l):
    return 4*l


# Area of Square
def calculateArea(l):
    return l*l


expression = input("Type a function: ")


for el in range(1, 5):
    if expression == 'calculatePerimeter(l)':
        print("If length is ", el, ", Perimeter = ", eval(expression))
    elif expression == 'calculateArea(l)':
        print("If length is ", el, ", Area = ", eval(expression))
    else:
        print('Wrong Function')
        break
