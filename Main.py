"""__Author__ = Matthew Zung
Welcome to my python lessons!
"""


def POGIL01():
    """
this is the basic print function.
    """
    print("Here is a example of the print function")
    print("You would type out print(whatever text you want) with quotations at"
          " front and back of the parenthesis.")
    print("You can use print statements to say anything")


def POGIL02():
    """
this is an example of input function and variables.
    """
    print("An example of using a variable is using the input statement.")
    name = input("What is your name? ")
    print("Your name is", name)


def POGIL03():
    """
this function will call and show you how arithmetic works
    """
    print("An example of arithmetic operations is this:")
    print("133 + 17")
    print(133 + 17)


def POGIL04():
    """
This function shows how the output of a function can be formatted a certain
way.
    """
    num_laptops = 7
    laptop_cost = 599.50
    price = num_laptops * laptop_cost
    print("Total cost of laptops: $", format(price, '.2f'))


def POGIL05():
    """
this is a not/true function that will run correctly if the statement is true.
    """
    num_books = 40
    if not num_books > 100:
        print("True")


def POGIL06():
    """
This is an example of a if statement
    """
    original_price = float(input("Enter the original cost of the item: "))
    sale_price = float(input("Enter the sale price: "))
    percent_off = int((original_price - sale_price) / original_price * 100)
    print("Original price: $", format(original_price, ".2f"), sep="")
    print("Sale price: $", format(sale_price, ".2f"), sep="")
    print("Percent off: ", format(percent_off, "d"), "%", sep="")
    if percent_off >= 50: print("You got a great sale!")


def POGIL07():
    """
This is an example of elif and if statements.
    """
    grade = int(input("Enter your grade: "))
    if grade >= 90:
        print("Very Good!")
    elif grade <= 89 >= 80:
        print("Good!")
    if grade < 80:
        print("Satisfactory")


def POGIL08():
    """
This is a example while loop.
    """
    countdown = 100
    while countdown > 0:
        print(countdown)
        countdown -= 1
    print("Done!")


def POGIL09():
    """
This is an example of a for loop.
    """
    total = 0
    for x in range(5):
        number = int(input("Enter a number: "))
        total += number
    print("The total is:", total)


def POGIL10():
    """
This is an example of a nested loop. Basically a loop in a loop.
    """
    height = int(input("Enter height: "))
    for row in range(1, height + 1):
        for column in range(row):
            print(row, end=" ")
        print()


def POGIL11():
    """
This function will use a pre defined function of math which is basic math
formulas as well as basic operations.
    """
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
    """
THis function will show how a void function works.
    """
    import math

    def calculate_area(radius):
        """

        :param radius: calculates the radius
        """
        area = math.pi * radius ** 2
        print("Area of a circle with a radius of", radius, "is",
              format(area, ".2f"))

    def main12():
        """
This function will calculate the area based on the radius size.
        """
        radius = int(input("Enter the radius: "))
        calculate_area(radius)

    main12()  # the call


def POGIL13():
    """
This function is a value returning function which is opposite to the void
function.

    """

    def get_smaller(num1, num2):
        """
this function will the the reason for choosing the smaller number.
        """
        if num1 < num2:
            smaller = num1
        else:
            smaller = num2
        return smaller

    def main13():
        """
this is the function that runs in the activity.
        """
        user_input1 = int(input("Enter a number: "))
        user_input2 = int(input("Enter a second number: "))

        smaller_number = get_smaller(user_input1, user_input2)
        print("The smaller number of the two numbers is", smaller_number)

    main13()  # the call again


def main_code():
    """
this code will run the entire program and start with a menu to select what you
want to do
    """
    print("Welcome to my python lessons!")
    user_wants_to_continue = True
    while user_wants_to_continue:
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
            user_wants_to_continue = False


main_code()
