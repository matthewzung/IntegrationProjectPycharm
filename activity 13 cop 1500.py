def getSmaller(num1,num2):
    if num1<num2:
        smaller = num1
    else:
        smaller = num2
    return smaller

def main():
    userInput1 = int(input("Enter a number: "))
    userInput2 = int(input("Enter a second number: "))

    smallerNumber = getSmaller(userInput1, userInput2)
    print("The smaller number of the two numbers is" , smallerNumber)


main()
