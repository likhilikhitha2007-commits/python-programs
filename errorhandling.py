try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    result=a/b
    print("Result:",result)
except ZeroDivisionError:
    print("Error:cannot divide by zero")
except ValueError:
    print("Error:Enter numbers only")