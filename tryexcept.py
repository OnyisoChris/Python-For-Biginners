#value = 10/0     #This brings a error

try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
#except:
    #print("Invalid Input")
except ZeroDivisionError as err: #catches specific errors.
    print("Divided by zero")
except ValueError:
    print("Invalid input")