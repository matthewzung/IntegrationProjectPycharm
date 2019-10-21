# Matthew Zung
# Welcome to my python lessons!

def POGIL01():
    print("Here is a example of the print function")
    print("You would type out print(whatever text you want) with quotations at the front and back of the parenthesis.")
    print("You can use print statements to say anything")

def POGIL02():
    print("An example of using a variable is using the input statement.")
    name = input("What is your name? ")
    print("Your name is", name)

def POGIL03():
    print("An example of arithmetic operations is this:")
    print("133 + 17")
    print(133 + 17)

def POGIL04():
    numLaptops = 7
    laptopCost = 599.50
    price = numLaptops * laptopCost
    print("Total cost of laptops: $", format(price, '.2f'))

def POGIL05():
    numBooks = 40
    not(numBooks * 10 ==100)

def POGIL06():
    originalPrice = float(input("Enter the original cost of the item: "))
    salePrice = float(input("Enter the sale price: "))
    percentOff = int((originalPrice - salePrice) / originalPrice * 100)
    print("Original price: $", format(originalPrice, ".2f"), sep="")
    print("Sale price: $", format(salePrice, ".2f"), sep="")
    print("Percent off: ", format(percentOff, "d"), "%", sep="")
    if percentOff >= 50: print("You got a great sale!")

def POGIL07():
    grade = int(input("Enter your grade: "))
    if grade >= 90:
        print("Very Good!")
    elif grade <= 89 >= 80:
        print("Good!")
    if grade < 80:
        print("Satisfactory")

def POGIL08():
    countdown = 100
    while countdown > 0:
        print(countdown)
        countdown = countdown - 1
    print("Done!")

def POGIL09():
    total = 0
    for x in range(5):
        number = int(input("Enter a number: "))
        total += number
    print("The total is:", total)

def POGIL10():
    height = int(input("Enter height: "))
    for row in range(1, height + 1):
        for column in range(row):
            print(row, end=" ")
        print()

def POGIL11():
    import math
    x = 4.7
    y = 5.3
    z = -4.8
    a = -3.2
    print(math.ceil(x))
    print(math.ceil(y))
    print(math.ceil(z))
    print(math.ceil(a))
    print(math.floor(x))
    print(math.floor(y))
    print(math.floor(z))
    print(math.floor(a))

def POGIL12():
    import math

    def calculateArea(radius):
        area = math.pi * radius ** 2
        print("Area of a circle with a radius of", radius, "is",
              format(area, ".2f"))

    def main12():
        radius = int(input("Enter the radius: "))
        calculateArea(radius)

    main12() #the call

def POGIL13():
    def getSmaller(num1, num2):
        if num1 < num2:
            smaller = num1
        else:
            smaller = num2
        return smaller

    def main13():
        userInput1 = int(input("Enter a number: "))
        userInput2 = int(input("Enter a second number: "))

        smallerNumber = getSmaller(userInput1, userInput2)
        print("The smaller number of the two numbers is", smallerNumber)

    main13() #the call again



def main():
    print("Welcome to my python lessons!")
    userWantsToContinue = True
    while userWantsToContinue:
        print("Enter a selection")
        print("1.Print Statements")
        print("2.Variables")
        print("3.Arithmetic Operations ")
        print("4.Formatting Outputs")
        print("5.Boolean Expressions")
        print("6.If else statements")
        print("7.Nested if else statements")
        print("8.While loops")
        print("9.For loops")
        print("10.Nested loops")
        print("11.Predefined functions")
        print("12.Void functions")
        print("13.Value returning functions")
        print("14. Exit")
        selection = int(input())
        if selection == 1:
            POGIL01()
        elif selection == 2:
            POGIL02()
        elif selection == 3:
            POGIL03()
        elif selection == 4:
            POGIL04()
        elif selection == 5:
            POGIL05()
        elif selection == 6:
            POGIL06()
        elif selection == 7:
            POGIL07()
        elif selection == 8:
            POGIL08()
        elif selection == 9:
            POGIL09()
        elif selection == 10:
            POGIL10()
        elif selection == 11:
            POGIL11()
        elif selection == 12:
            POGIL12()
        elif selection == 13:
            POGIL13()
        elif selection == 14:
            userWantsToContinue = False



main()
